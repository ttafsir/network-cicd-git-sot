import fnmatch
import logging
import re
import sys
import typing as t
from pathlib import Path

import yaml

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.NOTSET)
ANSIBLE_INVENTORY_DIR = Path("ansible/inventory")
PERSISTENT_DATADIR = Path("data")
DEVICE_PATTERNS = {
    "leaf": re.compile(r"(leaf)([0-9]{2}(?:_.*|-.*))"),
    "spine": re.compile(r"(spine)([0-9]{2}(?:_.*|-.*))"),
}
INVENTORY_MAP = {
    "spine": ["bgp", "system", "topology"],
    "leaf": ["bgp", "system", "topology", "layer2"],
}


def find_file_by_patterns(patterns: t.List, path: Path) -> t.List[str]:
    files = []
    for pattern in patterns:
        filenames = (str(p) for p in path.iterdir())
        files.extend(fnmatch.filter(filenames, pattern))
    return files


def load_yaml_documents(path: Path) -> t.Dict:
    """
    Find all yaml (*.yml, *.yaml) files in path and load them as yaml documents.
    Return a dict of documents, keyed by filename
    """
    files = find_file_by_patterns(["*.yml", "*.yaml"], path)
    return {
        Path(f).stem: yaml.load(Path(f).open(), Loader=yaml.FullLoader) for f in files
    }


def build_device_dir_structure(inventory: t.Dict) -> None:
    for device, data in inventory.items():
        host_vars_dir = ANSIBLE_INVENTORY_DIR / data["env"] / "host_vars" / device
        persistent_data = load_yaml_documents(PERSISTENT_DATADIR)

        if not host_vars_dir.exists():
            LOG.info(f"=> creating host vars dir for {device}")
            host_vars_dir.mkdir(parents=True)

        if location := data["location"]:
            create_group_vars_dir(location, data["env"])

        if platform := data["platform"]:
            create_group_vars_dir(platform, data["env"])
            platform_vars_dir = (
                ANSIBLE_INVENTORY_DIR / data["env"] / "group_vars" / platform
            )
            if platform_vars_dir.exists() and platform in persistent_data["platforms"]:
                connection_file = platform_vars_dir / "platform.yml"
                connection_file.write_text(
                    yaml.dump(persistent_data["platforms"][platform])
                )

        if role := data["role"]:
            for file_type in INVENTORY_MAP[role]:
                inventory_file = host_vars_dir / f"{file_type}.yaml"
                if not inventory_file.exists():
                    inventory_file.touch()
            create_group_vars_dir(role, data["env"])


def create_group_vars_dir(group: str, env: str) -> None:
    path = ANSIBLE_INVENTORY_DIR / env / "group_vars" / group
    if not path.exists():
        LOG.info(f"=> creating group_vars dir for {env}/{group}")
        path.mkdir(parents=True)


def build_environ_inventory(inventory: t.Dict, config: t.Dict = None) -> None:
    for device in inventory:
        role = inventory[device]["role"]
        location = inventory[device]["location"]

        # add device and vars to role group
        config[role].append({device: inventory[device]})

        # add device to platform group
        if platform := inventory[device]["platform"]:
            config[platform].append(device)

        # add role to location group
        if role not in config[location]:
            LOG.debug(f"Adding {role} to {location} group")
            config[location].append(device)


def initialize_environ_groups(inventory: t.Dict, config: t.Dict) -> None:
    device_roles = {d["role"] for _, d in inventory.items()}
    device_locations = {d["location"] for _, d in inventory.items()}
    platforms = {d["platform"] for _, d in inventory.items() if d["platform"]}

    for loc in device_locations:
        config[loc] = []

    for role in device_roles:
        config[role] = []

    for platform in platforms:
        config[platform] = []


def write_ini_inventories(ini_inventories: t.Dict) -> None:
    for environment in ini_inventories:
        path = Path(ini_inventories[environment]["path"])
        config = ini_inventories[environment]["config"]

        LOG.info(f"=> inventory file for {environment} to {path}")
        with path.open("w") as f:
            for group, group_members in config.items():
                write_group_to_ini(f, group)
                if group_members:
                    write_group_members_to_ini(group_members, f, skip=["env"])
                f.write("\n")


def write_group_to_ini(f, group: str):
    LOG.debug(f"=> writing group {group}")
    f.write("[{}]\n".format(group))


def write_group_members_to_ini(members: t.List, f, skip: t.List = None):
    skip_list = list(skip) if skip else []
    for member in members:
        # add hostname to group
        if isinstance(member, str):
            f.write(f"{member}")
        # add hostname and vars to group. ex "host1 ansible_host=1.1.1.1 location=dc1"
        elif isinstance(member, dict):
            for hostname, data in member.items():
                f.write(f"{hostname} ")
                for k, v in data.items():
                    if k not in skip_list or v is not None:
                        LOG.debug(f"=> writing {k}={v}")
                        f.write(f" {k}={v}")
        f.write("\n")


def get_device_role(device: str) -> str:
    for role, pattern in DEVICE_PATTERNS.items():
        match = pattern.match(device)
        if match:
            return role
    raise ValueError(f"{device} does not match any device pattern")


def process_devices_data(device_list: t.List[t.Dict]) -> t.Dict:
    return_dict = {}
    for device in device_list:
        name = device["name"]
        device["role"] = get_device_role(name)
        device["env"] = device.get("env", "production")
        device["platform"] = device.get("platform")
        device["location"] = name.split("-")[1] if len(name.split("-")) > 1 else None
        device["ansible_host"] = device.get("ip", "").split("/")[0]
        return_dict[name] = device
    return return_dict


def build_ini_inventory_dict(devices_dict: t.Dict) -> t.Dict:
    ini_inventories = {}

    # create host_vars dir and group_vars based on role and platform
    build_device_dir_structure(devices_dict)

    for env in {d["env"] for d in devices_dict.values()}:
        env_hostfile = ANSIBLE_INVENTORY_DIR / env / "hosts.ini"
        ini_inventories[env] = {"config": {}, "path": env_hostfile}

        for location in (
            d["location"] for d in devices_dict.values() if d["env"] == env
        ):
            ini_inventories[env]["config"].update({location: []})

        environ_inv = ini_inventories[env]["config"]
        env_devices_dict = {k: v for k, v in devices_dict.items() if v["env"] == env}
        initialize_environ_groups(env_devices_dict, environ_inv)
        build_environ_inventory(env_devices_dict, environ_inv)
    return ini_inventories


def main(devicefile: str):
    LOG.info("Loading device inventory...")
    input_data = yaml.load(Path(devicefile).read_text(), Loader=yaml.SafeLoader)
    devices_list = input_data["devices"]

    # parse devices and prepare inventory
    LOG.info("Parsing input data...")
    devices_dict = process_devices_data(devices_list)

    LOG.info("Building inventory...")
    ini_inventories = build_ini_inventory_dict(devices_dict)

    LOG.info("Writing inventory files...")
    write_ini_inventories(ini_inventories)


if __name__ == "__main__":
    args = sys.argv[1:]
    device_file = args[0] if len(args) >= 1 else "devices.yaml"
    options = args[1:] if len(args) > 1 else []

    if "--debug" in options:
        LOG.setLevel(logging.DEBUG)
    if "--info" in options:
        LOG.setLevel(logging.INFO)

    main(devicefile=device_file)
