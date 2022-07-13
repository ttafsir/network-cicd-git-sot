import logging

import pytest


def test_bgp_asn_matches_inventory(helpers, host, config_intent):
    """
    Arrange/Act: retrieve "ip bgp summary" output from device. Retrieve
        BGP intent from AVD intended design.
    Assert: The configured ASN matches the inventory ASN
    """
    if not config_intent.get("router_bgp"):
        pytest.skip("BGP is not expected on this device")

    output = helpers.cli_command(host, "show ip bgp summary | json")
    logging.debug("BGP output: %s", output)
    actual = helpers.dpath_get(output, "json/vrfs/default/asn")
    expected = helpers.dpath_get(config_intent, "router_bgp/as")
    assert actual == expected, f"ASN mismatch: {actual} != {expected}"


def test_bgp_multi_agent_is_enabled(host, helpers, config_intent):
    """
    Arrange/Act: retrieve "ip route summary" output from device.
    Assert: The configured ArBGP multi-agent is enabled
    """
    if not config_intent.get("router_bgp") or not config_intent.get(
        "service_routing_protocols_model"
    ):
        pytest.skip("Not Applicable for this device")
    output = helpers.cli_command(host, "show ip route summary")
    logging.debug("IP Route output: %s", output)
    assert "multi-agent" in output["stdout"]


@pytest.mark.parametrize(
    "show_command",
    ["show ip bgp summary | json", "show bgp evpn summary | json"],
    ids=["bgp", "evpn"],
)
def test_bgp_expected_peers_are_established(helpers, show_command, host, config_intent):
    """
    Arrange/Act: retrieve IPv4 and evpn BGP output from device. Retrieve
        BGP intent from AVD intended design.
    Assert: The configured expected peers are established for IPv4 and EVPN
    """
    if not config_intent.get("router_bgp"):
        pytest.skip("BGP is not expected on this device")

    logging.debug("Running command: %s", show_command)
    output = helpers.cli_command(host, show_command)
    logging.debug("Output: %s", output)
    actual = helpers.dpath_get(output, "json/vrfs/default/peers")
    expected = helpers.dpath_get(config_intent, "router_bgp/neighbors")
    assert (
        actual[neighbor]["peerState"] == "Established"
        for neighbor, _ in expected.items()
    )
