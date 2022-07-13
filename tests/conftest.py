import csv
import typing
from functools import lru_cache
from pathlib import Path

import dpath.util as dpath_util
import pytest
import testinfra
import yaml
from ntc_templates.parse import parse_output


@pytest.fixture(scope="module")
def eos_facts(host):
    """Retrieve facts from the device"""
    return host.ansible("arista.eos.eos_facts", 'gather_subset="min"')


@pytest.fixture(scope="module")
def host_vars(host):
    """Retrieve host variables from the inventory"""
    return host.ansible.get_variables()


def load_avd_structured_configs(inventory_dir: Path):
    """Load the structured config data from the AVD documentation directory"""
    relative_path = inventory_dir / "intended/structured_configs"
    absolute_path = Path(__file__).parent.parent / relative_path

    # find the yaml files in the directory
    yaml_files = absolute_path.glob("*.yml")
    return {f.stem: yaml.safe_load(f.read_text()) for f in yaml_files}


@pytest.fixture(scope="module")
def avd_structured_configs(request):
    """
    Load yaml data files from inventory_dir/intended/structured_configs,
    where each file represents a structured config. Returns  a dictionary
    with the file stem as the key and the value as the yaml data.
    """
    inventory_dir = Path(request.config.getoption("ansible_inventory")).parent
    return load_avd_structured_configs(inventory_dir)


@pytest.fixture(scope="module")
def config_intent(host_vars, avd_structured_configs):
    """Retrieve config intent from the device"""
    hostname = host_vars["inventory_hostname"]
    return avd_structured_configs[hostname]


@pytest.fixture(scope="module")
def get_host_intent(avd_structured_configs):
    """Retrieve config intent for a passed device"""

    def _get_intent(hostname):
        return avd_structured_configs[hostname]

    return _get_intent


def _load_avd_fabric_data(inventory_dir: Path, file_pattern: str):
    """Load the topology intent data from the AVD documentation directory"""
    relative_path = inventory_dir / "documentation/fabric"
    absolute_path = Path(__file__).parent.parent / relative_path

    # find the p2p and topology csv files in the directory
    csv_file = next(
        (path for path in absolute_path.glob("*.csv") if file_pattern in path.name),
        None,
    )

    reader_rows = None
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader_rows = tuple(csv.DictReader(f))
    return reader_rows


def _get_loopback0_intent(inventory_dir):
    """Retrieve the loopback0 address from intented configs for the fabric"""
    config_data = load_avd_structured_configs(inventory_dir)
    loopbacks = [
        v["loopback_interfaces"]
        for _, v in config_data.items()
        if v.get("loopback_interfaces")
    ]
    return [
        x["Loopback0"] for x in loopbacks if x.get("Loopback0", {}).get("ip_address")
    ]


def _get_vtep_reachability(inventory_dir):
    """Load the vtep intent data from the AVD documentation directory"""
    config_data = load_avd_structured_configs(inventory_dir)
    vxlan_interfaces = [
        (k, dpath_util.get(v, "vxlan_interface/Vxlan1/vxlan/source_interface"))
        for k, v in config_data.items()
        if v.get("vxlan_interface")
    ]
    return [
        config_data[k]["loopback_interfaces"][v].get("ip_address")
        for k, v in vxlan_interfaces
    ]


def _get_topology_intent(hosts, inventory_dir, file_pattern="topology"):
    """Load the topology intent data from the AVD documentation directory"""
    for host in hosts:
        hostname = host.backend.get_hostname()
        link_data = _load_avd_fabric_data(inventory_dir, file_pattern)
        for row in link_data:
            if row["Node"] == hostname:
                yield {k.lower().replace(" ", "_"): v for k, v in row.items()}


def topology_id_func(intent: dict):
    """ID function for pytest parametrization"""
    return (
        f"{intent['node']}-{intent['node_interface']}->"
        f"{intent['peer_node']}-{intent['peer_interface']}"
    )


def pytest_generate_tests(metafunc):
    """
    Set up parametrization for the topology intent data.
    """
    topology_fixtures = (
        "topology_intent",
        "p2p_link_intent",
        "loopback_intent",
        "vtep_intent",
    )
    if any(f in metafunc.fixturenames for f in topology_fixtures):
        ansible_inventory = metafunc.config.getoption("ansible_inventory")
        ansible_inventory_dir = Path(ansible_inventory).parent

        hosts = testinfra.get_hosts(
            ["all"],
            connection=metafunc.config.option.connection,
            ssh_config=metafunc.config.option.ssh_config,
            ssh_identity_file=metafunc.config.option.ssh_identity_file,
            sudo=metafunc.config.option.sudo,
            sudo_user=metafunc.config.option.sudo_user,
            ansible_inventory=metafunc.config.option.ansible_inventory,
            force_ansible=metafunc.config.option.force_ansible,
        )

        # parameterize the "topology_intent" fixture
        if "topology_intent" in metafunc.fixturenames:
            topology = _get_topology_intent(hosts, ansible_inventory_dir, "topology")
            metafunc.parametrize("topology_intent", topology, ids=topology_id_func)

        # parameterize the "p2p_link_intent" fixture
        if "p2p_link_intent" in metafunc.fixturenames:
            p2p_links = _get_topology_intent(hosts, ansible_inventory_dir, "p2p")
            metafunc.parametrize("p2p_link_intent", p2p_links, ids=topology_id_func)

        # parameterize the "config_intent" fixture
        if "loopback_intent" in metafunc.fixturenames:
            loopbacks = _get_loopback0_intent(ansible_inventory_dir)
            ids = map(
                lambda x: f"ping_{x.get('ip_address') if x else 'ping_None'}", loopbacks
            )
            metafunc.parametrize("loopback_intent", loopbacks, ids=ids)

        # parameterize the "vtep_intent" fixture
        if "vtep_intent" in metafunc.fixturenames:
            vteps = _get_vtep_reachability(ansible_inventory_dir)
            ids = map(lambda x: f"ping_{x or 'ping_None'}", vteps)
            metafunc.parametrize("vtep_intent", vteps, ids=ids)


class Helpers:
    """Helper functions for CLI tests."""

    @staticmethod
    @lru_cache
    def eos_show_command(node, commands: str, check_mode: bool = True):
        """Helper function to Run CLI command."""
        return node.ansible(
            "arista.eos.eos_command", f"commands='{commands}'", check=check_mode
        )

    @staticmethod
    @lru_cache
    def cli_command(node, commands: str, check_mode: bool = True):
        """Helper function to Run CLI command."""
        return node.ansible(
            "ansible.netcommon.cli_command", f"command='{commands}'", check=check_mode
        )

    @staticmethod
    def parse_command(
        command: str = None, output: str = None, platform: str = None
    ) -> dict:
        """Retrieve facts from the device"""
        return parse_output(
            platform=platform,
            command=command,
            data=output,
        )

    @staticmethod
    def dpath_get(data: dict, path: typing.Union[str, list]):
        """Helper function to get data from dpath"""
        return dpath_util.get(data, path)

    @staticmethod
    def dpath_search(data: dict, path: typing.Union[str, list]):
        """Helper function to search data from dpath"""
        return dpath_util.search(data, path)


@pytest.fixture(scope="session")
def helpers():
    """returns a Helpers object as a fixture."""
    return Helpers
