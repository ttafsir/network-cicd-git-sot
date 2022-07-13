import logging

import pytest


def test_vtep_ip_in_routing_table(host, helpers, host_vars, vtep_intent):
    """
    Arrange/Act:
    """
    if host_vars["type"] == "l2leaf":
        pytest.skip(reason="Test is not applicable on l2leafs")

    command = f"show ip route {vtep_intent} | json"
    logging.info("Running command: %s", command)
    output = helpers.cli_command(host, command, check_mode=False)
    logging.info("Output: %s", output)
    assert f"{vtep_intent}" in output["stdout"]
