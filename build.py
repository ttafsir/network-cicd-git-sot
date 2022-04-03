import contextlib
import configparser
from pathlib import Path
import logging
import string
import typing as t
import re
import sys

import yaml

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())
LOG.setLevel(logging.NOTSET)
ANSIBLE_INVENTORY_DIR = Path("ansible/inventory")
DEVICE_PATTERNS = {
    "leaf": re.compile(r"(leaf)([0-9]{2}-.*)"),
    "spine": re.compile(r"(spine)([0-9]{2}-.*)"),
}
INVENTORY_MAP = {
    "spine": ["bgp", "system", "topology"],
    "leaf": ["bgp", "system", "topology", "layer2"],
}


def build_device_dir_structure(
    device: str, env: str, role: str = None, location: str = None
) -> None:
    host_vars_dir = ANSIBLE_INVENTORY_DIR / env / "host_vars" / device
    if location:
        group_vars_dir = ANSIBLE_INVENTORY_DIR / env / location

    with contextlib.suppress(FileExistsError, NameError):
        host_vars_dir.mkdir(parents=True)
        group_vars_dir.mkdir(parents=True)

    if role:
        for file_type in INVENTORY_MAP[role]:
            inventory_file = host_vars_dir / f"{file_type}.yaml"
            if not inventory_file.exists():
                inventory_file.touch()


def build_inventory_config(inventory: t.Dict, config: t.Dict = None) -> None:
    initialize_groups(inventory, config)
    for device in inventory:
        role = inventory[device]["role"]
        location = inventory[device]["location"]

        # add device to role group
        config[role].append({device: inventory[device]})

        # add role to location group
        if role not in config[location]:
            LOG.info(f"Adding {role} to {location} group")
            config[location].append(device)


def initialize_groups(inventory, config):
    device_roles = {data["role"] for _, data in inventory.items()}
    device_locations = {data["location"] for _, data in inventory.items()}

    for loc in device_locations:
        config[loc] = []

    for role in device_roles:
        config[role] = []


def write_ini_inventories(ini_inventories: t.Dict) -> None:
    for environment in ini_inventories:
        path = ini_inventories[environment]["path"]
        config = ini_inventories[environment]["config"]
        LOG.info(f"Writing inventory file for {environment} to {path}")

        with Path(path).open("w") as f:
            for group, group_members in config.items():
                write_group_to_ini(f, group)
                if group_members:
                    write_group_members_to_ini(group_members, f, skip=["env"])
                f.write("\n")


def write_group_to_ini(f, group):
    LOG.debug(f"Writing group {group}")
    f.write("[{}]\n".format(group))


def write_group_members_to_ini(members, file, skip: t.List = None):
    skip_list = list(skip) if skip else []

    for member in members:
        LOG.debug(f"Writing device {member}")
        if isinstance(member, str):
            file.write(f"{member}")
        elif isinstance(member, dict):
            for hostname, data in member.items():
                file.write(f"{hostname} ")

                for k, v in data.items():
                    if k not in skip_list or v is not None:
                        LOG.debug(f"Writing {k}={v}")
                        file.write(f" {k}={v}")
        file.write("\n")


def build_ini_inventory(devices: t.Dict) -> t.Dict:
    LOG.info("Building inventory...")
    inventory_dict = {}
    ini_inventories = {}
    seen = set()
    for record in devices:
        dev_name, env, dev_ip, location = parse_device_record(record)

        if env not in ini_inventories:
            ini_inventories[env] = {"path": "", "config": {}}

        # add location to inventory. we'll add as a group later
        if location is not None and (env, location) not in seen:
            ini_inventories[env]["config"].update({location: []})
        seen.add((env, location))

        # Build the device directory structure for the device
        for role, regex in DEVICE_PATTERNS.items():
            if regex.match(dev_name):
                inventory_dict[dev_name] = {
                    "role": role,
                    "env": env,
                    "location": location,
                    "ansible_host": dev_ip.split("/")[0],
                }
                LOG.debug(f"Building {dev_name} dir structure")
                build_device_dir_structure(dev_name, env, role=role, location=location)
        build_inventory_config(inventory_dict, ini_inventories[env]["config"])
        ini_inventories[env]["path"] = ANSIBLE_INVENTORY_DIR / env / "hosts.ini"
    return ini_inventories


def parse_device_record(record):
    dev_name = record["name"]
    env = record.get("env", "production")
    dev_ip = record.get("ip")
    location = dev_name.split("-")[1] if len(dev_name.split("-")) > 1 else None
    return dev_name, env, dev_ip, location


def main(devicefile: str):
    LOG.info("Loading device inventory...")
    devices_data = yaml.load(Path(devicefile).read_text(), Loader=yaml.SafeLoader)
    devices = devices_data["devices"]

    ini_inventories = build_ini_inventory(devices)
    LOG.debug(ini_inventories)
    write_ini_inventories(ini_inventories)


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) >= 1:
        device_file = args[0]
        options = args[1:] if len(args) > 1 else []
    else:
        device_file = "devices.yaml"
        options = []

    if "--debug" in options:
        LOG.setLevel(logging.DEBUG)

    if "--info" in options:
        LOG.setLevel(logging.INFO)

    main(devicefile=device_file)
