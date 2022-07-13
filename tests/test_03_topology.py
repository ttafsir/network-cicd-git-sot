from functools import lru_cache

import pytest
import testinfra

from .avd_links import get_link


@lru_cache
def gather_interface_facts(node):
    """Gather interface facts from the device"""
    return node.ansible("arista.eos.eos_facts", 'gather_subset="interfaces"')


def test_links_are_connected(topology_intent, request):
    """
    Arrange/Act: Load the <fabric>-topology.csv from the generated AVD
                documentation directory as the topology intent and validate
                that the configured links match the intent.
    Assert: The interface is connected
    """
    ansible_inventory = request.config.getoption("ansible_inventory")
    link = get_link(topology_intent, "link")

    # Retrieve the interface facts from the device
    node = testinfra.get_host(
        f"ansible://{link.node}?ansible_inventory={ansible_inventory}",
    )
    output = gather_interface_facts(node)
    try:
        node_interface_facts = output["ansible_facts"]["ansible_net_interfaces"]
    except KeyError:
        pytest.fail(output.get("msg"))

    assert node_interface_facts[link.node_interface]["operstatus"] == "connected"


def test_links_neighbors_match_intent(topology_intent, request):
    """
    Arrange/Act: Load the <fabric>-topology.csv from the generated AVD
                documentation directory as the topology intent and validate
                that the configured links match the intent.
    Assert: The intended neighbors are found on the links
    """
    ansible_inventory = request.config.getoption("ansible_inventory")
    link = get_link(topology_intent, "link")

    # Retrieve the interface facts from the device
    node = testinfra.get_host(
        f"ansible://{link.node}?ansible_inventory={ansible_inventory}",
    )
    output = gather_interface_facts(node)

    try:
        node_neighbors_facts = output["ansible_facts"]["ansible_net_neighbors"]
    except KeyError:
        pytest.fail(output.get("msg"))

    # get neighbors for the a-side of the link
    link_neighbors = [
        (link["host"], link["port"])
        for link in node_neighbors_facts.get(link.node_interface, [])
    ]

    # validate that the a-side of the link has the b-side as a neighbor
    expected_neighbor = (link.peer_node, link.peer_interface)
    assert expected_neighbor in link_neighbors


def test_p2p_l3_links_match_intent(p2p_link_intent, request):
    """
    Arrange/Act: Load the <fabric>-p2p-links.csv from the generated AVD
            documentation directory as the topology intent and validate
            that the configured p2p links match the intent.
    Assert: The configured IP/mask address matches intent the P2P link
    """
    ansible_inventory = request.config.getoption("ansible_inventory")
    link = get_link(p2p_link_intent, "p2p_link")
    node = testinfra.get_host(
        f"ansible://{link.node}?ansible_inventory={ansible_inventory}",
    )

    # Retrieve the interface facts from the device
    output = gather_interface_facts(node)
    try:
        node_interface_facts = output["ansible_facts"]["ansible_net_interfaces"]
    except KeyError:
        pytest.fail(output.get("msg"))

    expect_ip, expect_ip_len = (
        link.leaf_ip_address.split("/", maxsplit=1)[0],
        link.leaf_ip_address.split("/")[1],
    )
    actual_ip = node_interface_facts[link.node_interface]["ipv4"]["address"]
    actual_ip_len = node_interface_facts[link.node_interface]["ipv4"]["masklen"]

    assert f"{actual_ip}/{actual_ip_len}" == f"{expect_ip}/{expect_ip_len}"
