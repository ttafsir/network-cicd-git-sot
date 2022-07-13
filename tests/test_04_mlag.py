import pytest


def test_mlag_state_is_active_and_connected(host, helpers, host_vars):
    """
    Arrange/Act: Retrieve mlag operational state from device
    Assert: MLAG is active and connected on l2 and l3 leafs
    """
    if host_vars["type"] not in ("l2leaf", "l3leaf"):
        pytest.skip("MLAG is not supported on this device")

    command = "show mlag detail | json"
    json_output = helpers.cli_command(host, command)
    assert json_output["json"]["state"] == "active", "MLAG is not active"
    assert json_output["json"]["negStatus"] == "connected", "MLAG is not connected"
