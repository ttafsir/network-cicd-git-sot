import pytest


@pytest.mark.xfail(reason="NTP is not yet configured")
def test_ntp_is_synchronised(host, helpers):
    """
    Arrange/Act: Retrieve facts from device and variables from inventory
    Assert: The configured ASN matches the inventory ASN
    """
    command = "show ntp status | json"
    json_output = helpers.cli_command(host, command)
    assert json_output["json"]["status"] == "synchronised", "NTP is not synchronised"
