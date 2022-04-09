from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
    name: avd_fabric
    plugin_type: inventory
    short_description: Returns Ansible inventory from AVD fabric design
    description: Returns Ansible inventory from AVD fabric design
    options:
      plugin:
          description: Name of the plugin
          required: true
          choices: ['avd_fabric']
      data_dir:
        description: Path to the directory containing the AVD fabric design
        required: true
      design:
        description: Name of the design. Should be the same as the directory name
        required: true
      device_patterns:
        description: List of regex patterns to match devices
        required: false
"""
import fnmatch
import typing as t
from pathlib import Path

import yaml
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin


class InventoryModule(BaseInventoryPlugin):
    NAME = "avd_fabric"  # used internally by Ansible, it should match the file name but not required

    def verify_file(self, path):
        """Return true/false if this is possibly a valid file for this plugin to
        consume

        """
        return bool(
            super(InventoryModule, self).verify_file(path)
            and path.endswith(("avd_fabric.yaml", "avd_fabric.yml"))
        )

    def populate(self):
        self.avd_inventory = self._load_design_directory(self.design)

    def set_hostvars_from_keyed_data(self, hostname: str, data: t.Dict) -> None:
        for varsfile in data.values():
            self.set_hostvars(hostname, varsfile)

    def set_hostvars(self, hostname, data):
        for key, value in data.items():
            self.inventory.set_variable(hostname, key, value)

    def _find_file_by_patterns(self, patterns: t.List, path: Path) -> t.List[str]:
        files = []
        for pattern in patterns:
            filenames = (str(p) for p in path.iterdir())
            files.extend(fnmatch.filter(filenames, pattern))
        return files

    def _load_yaml_documents(self, path: Path) -> t.List[dict]:
        """
        Find all yaml (*.yml, *.yaml) files in path and load them as yaml documents.
        Return a dict of documents, keyed by filename
        """
        files = self._find_file_by_patterns(["*.yml", "*.yaml"], path)
        return {
            Path(f).stem: yaml.load(Path(f).open(), Loader=yaml.FullLoader)
            for f in files
        }

    def _load_node_data(self, fabric_name: str, fabric_dir: Path) -> t.Dict:
        """Return the node_group inventory"""
        node_group_dir = fabric_dir / fabric_name / "node_groups"
        node_detail_dir = fabric_dir / fabric_name / "nodes"

        node_groups = {}
        if node_group_dir.is_dir():
            node_groups = self._load_yaml_documents(node_group_dir)

        node_details = {}
        if node_detail_dir.is_dir():
            node_details = self._load_yaml_documents(node_detail_dir)

        return node_groups, node_details

    def _load_device_vars(
        self,
        device_dict: t.Dict,
        fabric_name: str,
        fabric_data,
        nodes: t.Dict,
        node_groups: t.Dict,
    ) -> None:
        for device_type, device_list in device_dict.items():
            self.inventory.add_group(device_type)

            if fabric_data.get(device_type):
                fabric_data[device_type][device_type].update({"node_groups": {}})

            for device in device_list:
                environment = device.get("env", "production")
                self.inventory.add_host(host=device["name"], group=fabric_name)
                if platform := device.get("platform"):
                    self.inventory.set_variable(device["name"], "platform", platform)
                self.inventory.set_variable(device["name"], "env", environment)
                self.inventory.set_variable(device["name"], "type", device_type)

                if node_data := nodes.get(device["name"]):
                    self.set_hostvars(device["name"], node_data)

    def _load_evpn(self, directory):
        """Return the EVPN inventory"""
        fabric_root = Path(directory) / "fabric"
        if not fabric_root.is_dir():
            raise AnsibleError(f"{directory} is not a directory")

        for subdir in fabric_root.iterdir():
            if subdir.is_dir():
                fabric_name = subdir.name
                self.inventory.add_group(fabric_name)

                fabric_data = self._load_yaml_documents(subdir)

                # parse switch node and node_group data
                node_groups, node_details = self._load_node_data(
                    fabric_name, fabric_root
                )

                # parse devices from `devices.yaml` and set host_vars
                if devices := fabric_data.pop("devices"):
                    self._load_device_vars(
                        devices,
                        fabric_name,
                        fabric_data,
                        nodes=node_details,
                        node_groups=node_groups,
                    )

                # set fabric vars
                self.set_hostvars_from_keyed_data(fabric_name, fabric_data)

    def _load_design_directory(self, design_directory):
        """Load yaml data from the design directory"""
        data_root = Path(self.data_dir)
        dir_path = data_root / design_directory
        if not dir_path.is_dir():
            raise AnsibleError(f"{design_directory} is not a directory")

        # yaml files in the top level data directory
        common_vars = self._load_yaml_documents(data_root)
        if common := common_vars.pop("common"):
            for key, value in common.items():
                self.inventory.set_variable("all", key, value)

        loader = getattr(self, f"_load_{self.design}")
        return loader(dir_path)

    def parse(self, inventory, loader, path, cache):

        super(InventoryModule, self).parse(inventory, loader, path, cache)
        # read inventory config file
        self._read_config_data(path)
        try:
            self.plugin = self.get_option("plugin")
            self.data_dir = self.get_option("data_dir")
            self.design = self.get_option("design")
            self.device_patterns = self.get_option("device_patterns")
        except Exception as e:
            raise AnsibleParserError(f"All correct options required: {e}") from e
        # Populate the inventory
        self.populate()
