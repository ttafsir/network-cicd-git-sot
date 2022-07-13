import logging
from ipaddress import ip_interface

import pytest
import testinfra

from .avd_links import get_link


def test_ethernet_link_neighbor_is_reachable(helpers, p2p_link_intent, request):
    """
    Arrange/Act:
    Assert: The link peer IPs are reachable on P2P links
    """
    inventory = request.config.getoption("ansible_inventory")
    link = get_link(p2p_link_intent, "p2p_link")
    node = testinfra.get_host(
        f"ansible://{link.node}?ansible_inventory={inventory}",
    )
    remote_ip = ip_interface(link.peer_ip_address)
    command = f"ping {remote_ip.ip} repeat 1"
    logging.info("Running command: %s", command)
    output = helpers.cli_command(node, command, check_mode=False)
    logging.info("Output: %s", output)
    assert "1 received" in output["stdout"]


def test_remote_loop0_ips_reachable_from_l3leafs(
    host, helpers, host_vars, config_intent, loopback_intent
):
    """
    Arrange: Retrieve configured loopback0 IPs from inventory
    Act: Ping each loopback IP from loopback0
    Assert: All loopback0 IPs can be reached from loopback0
    """
    if host_vars["type"] != "l3leaf":
        pytest.skip(reason="This test is only for l3 leaf devices")

    remote_l0 = ip_interface(loopback_intent["ip_address"])
    local_l0 = ip_interface(
        helpers.dpath_get(config_intent, "loopback_interfaces/Loopback0/ip_address")
    )
    command = f"ping {remote_l0.ip} source {local_l0.ip} repeat 1"
    logging.info("Running command: %s", command)
    output = helpers.cli_command(host, command, check_mode=False)
    logging.info("Output: %s", output)
    assert "1 received" in output["stdout"]
