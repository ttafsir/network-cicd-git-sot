def test_hostname_matches_inventory(eos_facts, host_vars):
    """
    Arrange/Act: Retrieve facts from device and variables from inventory
    Assert: The configured hostname matches the inventory hostname
    """
    actual = eos_facts["ansible_facts"]["ansible_net_hostname"]
    expected = host_vars["inventory_hostname"]
    assert actual == expected, f"Hostname mismatch: {actual} != {expected}"


def test_software_version(eos_facts, host_vars):
    """
    Arrange/Act: Retrieve facts from device and variables from inventory
    Assert: The current matches the inventory version
    """
    actual = eos_facts["ansible_facts"]["ansible_net_version"]
    expected = host_vars["ios_version"]
    assert actual == expected, f"Version mismatch: {actual} != {expected}"
