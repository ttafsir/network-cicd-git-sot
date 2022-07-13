
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 258 | 246 | 12 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| leaf01-dc1 |  38 | 37 | 1 | NTP |
| leaf02-dc1 |  38 | 37 | 1 | NTP |
| leaf03-dc1 |  43 | 42 | 1 | NTP |
| leaf04-dc1 |  43 | 42 | 1 | NTP |
| leaf05-dc1 |  15 | 12 | 3 | NTP, Routing Table |
| leaf06-dc1 |  15 | 12 | 3 | NTP, Routing Table |
| spine01-dc1 |  33 | 32 | 1 | NTP |
| spine02-dc1 |  33 | 32 | 1 | NTP |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  8 | 0 | 8 |
| Interface State |  86 | 86 | 0 |
| LLDP Topology |  36 | 36 | 0 |
| MLAG |  6 | 6 | 0 |
| IP Reachability |  16 | 16 | 0 |
| BGP |  42 | 42 | 0 |
| Routing Table |  40 | 36 | 4 |
| Loopback0 Reachability |  24 | 24 | 0 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf01-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 2 | leaf02-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 3 | leaf03-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 4 | leaf04-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 5 | leaf05-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 6 | leaf06-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 7 | spine01-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 8 | spine02-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 203 | leaf05-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | FAIL | VTEP 192.168.254.3 is not in the routing table |
| 204 | leaf05-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | FAIL | VTEP 192.168.254.5 is not in the routing table |
| 205 | leaf06-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | FAIL | VTEP 192.168.254.3 is not in the routing table |
| 206 | leaf06-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | FAIL | VTEP 192.168.254.5 is not in the routing table |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | leaf01-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 2 | leaf02-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 3 | leaf03-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 4 | leaf04-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 5 | leaf05-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 6 | leaf06-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 7 | spine01-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 8 | spine02-dc1 | NTP | Synchronised with NTP server | NTP | FAIL | not synchronised to NTP server |
| 9 | leaf01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf02-dc1_Ethernet3 | PASS | - |
| 10 | leaf01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - MLAG_PEER_leaf02-dc1_Ethernet4 | PASS | - |
| 11 | leaf01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE01-DC1_Ethernet1 | PASS | - |
| 12 | leaf01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE02-DC1_Ethernet1 | PASS | - |
| 13 | leaf02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf01-dc1_Ethernet3 | PASS | - |
| 14 | leaf02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - MLAG_PEER_leaf01-dc1_Ethernet4 | PASS | - |
| 15 | leaf02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE01-DC1_Ethernet2 | PASS | - |
| 16 | leaf02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE02-DC1_Ethernet2 | PASS | - |
| 17 | leaf03-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf04-dc1_Ethernet3 | PASS | - |
| 18 | leaf03-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - MLAG_PEER_leaf04-dc1_Ethernet4 | PASS | - |
| 19 | leaf03-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE01-DC1_Ethernet3 | PASS | - |
| 20 | leaf03-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE02-DC1_Ethernet3 | PASS | - |
| 21 | leaf03-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - LEAF05-DC1_Ethernet1 | PASS | - |
| 22 | leaf03-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet6 - LEAF06-DC1_Ethernet1 | PASS | - |
| 23 | leaf04-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf03-dc1_Ethernet3 | PASS | - |
| 24 | leaf04-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - MLAG_PEER_leaf03-dc1_Ethernet4 | PASS | - |
| 25 | leaf04-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_SPINE01-DC1_Ethernet4 | PASS | - |
| 26 | leaf04-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_SPINE02-DC1_Ethernet4 | PASS | - |
| 27 | leaf04-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 - LEAF05-DC1_Ethernet2 | PASS | - |
| 28 | leaf04-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet6 - LEAF06-DC1_Ethernet2 | PASS | - |
| 29 | leaf05-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf06-dc1_Ethernet3 | PASS | - |
| 30 | leaf05-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - MLAG_PEER_leaf06-dc1_Ethernet4 | PASS | - |
| 31 | leaf05-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - LEAF03-DC1_Ethernet5 | PASS | - |
| 32 | leaf05-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - LEAF04-DC1_Ethernet5 | PASS | - |
| 33 | leaf06-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - MLAG_PEER_leaf05-dc1_Ethernet3 | PASS | - |
| 34 | leaf06-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - MLAG_PEER_leaf05-dc1_Ethernet4 | PASS | - |
| 35 | leaf06-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - LEAF03-DC1_Ethernet6 | PASS | - |
| 36 | leaf06-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - LEAF04-DC1_Ethernet6 | PASS | - |
| 37 | spine01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF01-DC1_Ethernet1 | PASS | - |
| 38 | spine01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF02-DC1_Ethernet1 | PASS | - |
| 39 | spine01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF03-DC1_Ethernet1 | PASS | - |
| 40 | spine01-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF04-DC1_Ethernet1 | PASS | - |
| 41 | spine02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 - P2P_LINK_TO_LEAF01-DC1_Ethernet2 | PASS | - |
| 42 | spine02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 - P2P_LINK_TO_LEAF02-DC1_Ethernet2 | PASS | - |
| 43 | spine02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 - P2P_LINK_TO_LEAF03-DC1_Ethernet2 | PASS | - |
| 44 | spine02-dc1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 - P2P_LINK_TO_LEAF04-DC1_Ethernet2 | PASS | - |
| 45 | leaf01-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf02-dc1_Po3 | PASS | - |
| 46 | leaf02-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf01-dc1_Po3 | PASS | - |
| 47 | leaf03-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf04-dc1_Po3 | PASS | - |
| 48 | leaf03-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - DC1_LEAF2_Po1 | PASS | - |
| 49 | leaf04-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf03-dc1_Po3 | PASS | - |
| 50 | leaf04-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel5 - DC1_LEAF2_Po1 | PASS | - |
| 51 | leaf05-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf06-dc1_Po3 | PASS | - |
| 52 | leaf05-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel1 - DC1_SVC01_Po5 | PASS | - |
| 53 | leaf06-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel3 - MLAG_PEER_leaf05-dc1_Po3 | PASS | - |
| 54 | leaf06-dc1 | Interface State | Port-Channel Interface Status & Line Protocol == "up" | Port-Channel1 - DC1_SVC01_Po5 | PASS | - |
| 55 | leaf01-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 56 | leaf01-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 57 | leaf01-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan110 - Tenant_A_OP_Zone_1 | PASS | - |
| 58 | leaf01-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan111 - Tenant_A_OP_Zone_2 | PASS | - |
| 59 | leaf01-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS | - |
| 60 | leaf02-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 61 | leaf02-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 62 | leaf02-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan110 - Tenant_A_OP_Zone_1 | PASS | - |
| 63 | leaf02-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan111 - Tenant_A_OP_Zone_2 | PASS | - |
| 64 | leaf02-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS | - |
| 65 | leaf03-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 66 | leaf03-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 67 | leaf03-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan112 - Tenant_A_OP_Zone_3 | PASS | - |
| 68 | leaf03-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan113 - Tenant_A_OP_Zone_4 | PASS | - |
| 69 | leaf03-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS | - |
| 70 | leaf04-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4093 - MLAG_PEER_L3_PEERING | PASS | - |
| 71 | leaf04-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 72 | leaf04-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan112 - Tenant_A_OP_Zone_3 | PASS | - |
| 73 | leaf04-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan113 - Tenant_A_OP_Zone_4 | PASS | - |
| 74 | leaf04-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan3009 - MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | PASS | - |
| 75 | leaf05-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 76 | leaf06-dc1 | Interface State | Vlan Interface Status & Line Protocol == "up" | Vlan4094 - MLAG_PEER | PASS | - |
| 77 | leaf01-dc1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 78 | leaf02-dc1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 79 | leaf03-dc1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 80 | leaf04-dc1 | Interface State | Vxlan Interface Status & Line Protocol == "up" | Vxlan1 | PASS | - |
| 81 | leaf01-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 82 | leaf01-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 83 | leaf01-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS | - |
| 84 | leaf02-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 85 | leaf02-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 86 | leaf02-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS | - |
| 87 | leaf03-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 88 | leaf03-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 89 | leaf03-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS | - |
| 90 | leaf04-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 91 | leaf04-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback1 - VTEP_VXLAN_Tunnel_Source | PASS | - |
| 92 | leaf04-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback100 - Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | PASS | - |
| 93 | spine01-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 94 | spine02-dc1 | Interface State | Loopback Interface Status & Line Protocol == "up" | Loopback0 - EVPN_Overlay_Peering | PASS | - |
| 95 | leaf01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf02-dc1_Ethernet3 | PASS | - |
| 96 | leaf01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf02-dc1_Ethernet4 | PASS | - |
| 97 | leaf01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: spine01-dc1_Ethernet1 | PASS | - |
| 98 | leaf01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: spine02-dc1_Ethernet1 | PASS | - |
| 99 | leaf02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf01-dc1_Ethernet3 | PASS | - |
| 100 | leaf02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf01-dc1_Ethernet4 | PASS | - |
| 101 | leaf02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: spine01-dc1_Ethernet2 | PASS | - |
| 102 | leaf02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: spine02-dc1_Ethernet2 | PASS | - |
| 103 | leaf03-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf04-dc1_Ethernet3 | PASS | - |
| 104 | leaf03-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf04-dc1_Ethernet4 | PASS | - |
| 105 | leaf03-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: spine01-dc1_Ethernet3 | PASS | - |
| 106 | leaf03-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: spine02-dc1_Ethernet3 | PASS | - |
| 107 | leaf03-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf05-dc1_Ethernet1 | PASS | - |
| 108 | leaf03-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf06-dc1_Ethernet1 | PASS | - |
| 109 | leaf04-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf03-dc1_Ethernet3 | PASS | - |
| 110 | leaf04-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf03-dc1_Ethernet4 | PASS | - |
| 111 | leaf04-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: spine01-dc1_Ethernet4 | PASS | - |
| 112 | leaf04-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: spine02-dc1_Ethernet4 | PASS | - |
| 113 | leaf04-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet5 - remote: leaf05-dc1_Ethernet2 | PASS | - |
| 114 | leaf04-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet6 - remote: leaf06-dc1_Ethernet2 | PASS | - |
| 115 | leaf05-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf06-dc1_Ethernet3 | PASS | - |
| 116 | leaf05-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf06-dc1_Ethernet4 | PASS | - |
| 117 | leaf05-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf03-dc1_Ethernet5 | PASS | - |
| 118 | leaf05-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf04-dc1_Ethernet5 | PASS | - |
| 119 | leaf06-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf05-dc1_Ethernet3 | PASS | - |
| 120 | leaf06-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf05-dc1_Ethernet4 | PASS | - |
| 121 | leaf06-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf03-dc1_Ethernet6 | PASS | - |
| 122 | leaf06-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf04-dc1_Ethernet6 | PASS | - |
| 123 | spine01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf01-dc1_Ethernet1 | PASS | - |
| 124 | spine01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf02-dc1_Ethernet1 | PASS | - |
| 125 | spine01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf03-dc1_Ethernet1 | PASS | - |
| 126 | spine01-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf04-dc1_Ethernet1 | PASS | - |
| 127 | spine02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet1 - remote: leaf01-dc1_Ethernet2 | PASS | - |
| 128 | spine02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet2 - remote: leaf02-dc1_Ethernet2 | PASS | - |
| 129 | spine02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet3 - remote: leaf03-dc1_Ethernet2 | PASS | - |
| 130 | spine02-dc1 | LLDP Topology | LLDP topology - validate peer and interface | local: Ethernet4 - remote: leaf04-dc1_Ethernet2 | PASS | - |
| 131 | leaf01-dc1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 132 | leaf02-dc1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 133 | leaf03-dc1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 134 | leaf04-dc1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 135 | leaf05-dc1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 136 | leaf06-dc1 | MLAG | MLAG State active & Status connected | MLAG | PASS | - |
| 137 | leaf01-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf01-dc1_Ethernet1 - Destination: spine01-dc1_Ethernet1 | PASS | - |
| 138 | leaf01-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf01-dc1_Ethernet2 - Destination: spine02-dc1_Ethernet1 | PASS | - |
| 139 | leaf02-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf02-dc1_Ethernet1 - Destination: spine01-dc1_Ethernet2 | PASS | - |
| 140 | leaf02-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf02-dc1_Ethernet2 - Destination: spine02-dc1_Ethernet2 | PASS | - |
| 141 | leaf03-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf03-dc1_Ethernet1 - Destination: spine01-dc1_Ethernet3 | PASS | - |
| 142 | leaf03-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf03-dc1_Ethernet2 - Destination: spine02-dc1_Ethernet3 | PASS | - |
| 143 | leaf04-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf04-dc1_Ethernet1 - Destination: spine01-dc1_Ethernet4 | PASS | - |
| 144 | leaf04-dc1 | IP Reachability | ip reachability test p2p links | Source: leaf04-dc1_Ethernet2 - Destination: spine02-dc1_Ethernet4 | PASS | - |
| 145 | spine01-dc1 | IP Reachability | ip reachability test p2p links | Source: spine01-dc1_Ethernet1 - Destination: leaf01-dc1_Ethernet1 | PASS | - |
| 146 | spine01-dc1 | IP Reachability | ip reachability test p2p links | Source: spine01-dc1_Ethernet2 - Destination: leaf02-dc1_Ethernet1 | PASS | - |
| 147 | spine01-dc1 | IP Reachability | ip reachability test p2p links | Source: spine01-dc1_Ethernet3 - Destination: leaf03-dc1_Ethernet1 | PASS | - |
| 148 | spine01-dc1 | IP Reachability | ip reachability test p2p links | Source: spine01-dc1_Ethernet4 - Destination: leaf04-dc1_Ethernet1 | PASS | - |
| 149 | spine02-dc1 | IP Reachability | ip reachability test p2p links | Source: spine02-dc1_Ethernet1 - Destination: leaf01-dc1_Ethernet2 | PASS | - |
| 150 | spine02-dc1 | IP Reachability | ip reachability test p2p links | Source: spine02-dc1_Ethernet2 - Destination: leaf02-dc1_Ethernet2 | PASS | - |
| 151 | spine02-dc1 | IP Reachability | ip reachability test p2p links | Source: spine02-dc1_Ethernet3 - Destination: leaf03-dc1_Ethernet2 | PASS | - |
| 152 | spine02-dc1 | IP Reachability | ip reachability test p2p links | Source: spine02-dc1_Ethernet4 - Destination: leaf04-dc1_Ethernet2 | PASS | - |
| 153 | leaf01-dc1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 154 | leaf02-dc1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 155 | leaf03-dc1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 156 | leaf04-dc1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 157 | spine01-dc1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 158 | spine02-dc1 | BGP | ArBGP is configured and operating | ArBGP | PASS | - |
| 159 | leaf01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.1 | PASS | - |
| 160 | leaf01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.0 | PASS | - |
| 161 | leaf01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.2 | PASS | - |
| 162 | leaf02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.0 | PASS | - |
| 163 | leaf02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.4 | PASS | - |
| 164 | leaf02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.6 | PASS | - |
| 165 | leaf03-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.5 | PASS | - |
| 166 | leaf03-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.8 | PASS | - |
| 167 | leaf03-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.10 | PASS | - |
| 168 | leaf04-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 10.255.251.4 | PASS | - |
| 169 | leaf04-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.12 | PASS | - |
| 170 | leaf04-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.14 | PASS | - |
| 171 | spine01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.1 | PASS | - |
| 172 | spine01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.5 | PASS | - |
| 173 | spine01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.9 | PASS | - |
| 174 | spine01-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.13 | PASS | - |
| 175 | spine02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.3 | PASS | - |
| 176 | spine02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.7 | PASS | - |
| 177 | spine02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.11 | PASS | - |
| 178 | spine02-dc1 | BGP | ip bgp peer state established (ipv4) | bgp_neighbor: 172.31.255.15 | PASS | - |
| 179 | leaf01-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.1 | PASS | - |
| 180 | leaf01-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.2 | PASS | - |
| 181 | leaf02-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.1 | PASS | - |
| 182 | leaf02-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.2 | PASS | - |
| 183 | leaf03-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.1 | PASS | - |
| 184 | leaf03-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.2 | PASS | - |
| 185 | leaf04-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.1 | PASS | - |
| 186 | leaf04-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.2 | PASS | - |
| 187 | spine01-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.3 | PASS | - |
| 188 | spine01-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.4 | PASS | - |
| 189 | spine01-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.5 | PASS | - |
| 190 | spine01-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.6 | PASS | - |
| 191 | spine02-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.3 | PASS | - |
| 192 | spine02-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.4 | PASS | - |
| 193 | spine02-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.5 | PASS | - |
| 194 | spine02-dc1 | BGP | bgp evpn peer state established (evpn) | bgp_neighbor: 192.168.255.6 | PASS | - |
| 195 | leaf01-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | PASS | - |
| 196 | leaf01-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | PASS | - |
| 197 | leaf02-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | PASS | - |
| 198 | leaf02-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | PASS | - |
| 199 | leaf03-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | PASS | - |
| 200 | leaf03-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | PASS | - |
| 201 | leaf04-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | PASS | - |
| 202 | leaf04-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | PASS | - |
| 203 | leaf05-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | FAIL | VTEP 192.168.254.3 is not in the routing table |
| 204 | leaf05-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | FAIL | VTEP 192.168.254.5 is not in the routing table |
| 205 | leaf06-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | FAIL | VTEP 192.168.254.3 is not in the routing table |
| 206 | leaf06-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | FAIL | VTEP 192.168.254.5 is not in the routing table |
| 207 | spine01-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | PASS | - |
| 208 | spine01-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | PASS | - |
| 209 | spine02-dc1 | Routing Table | Remote VTEP address | 192.168.254.3 | PASS | - |
| 210 | spine02-dc1 | Routing Table | Remote VTEP address | 192.168.254.5 | PASS | - |
| 211 | leaf01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.3 | PASS | - |
| 212 | leaf01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.4 | PASS | - |
| 213 | leaf01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.5 | PASS | - |
| 214 | leaf01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.6 | PASS | - |
| 215 | leaf02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.3 | PASS | - |
| 216 | leaf02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.4 | PASS | - |
| 217 | leaf02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.5 | PASS | - |
| 218 | leaf02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.6 | PASS | - |
| 219 | leaf03-dc1 | Routing Table | Remote Lo0 address | 192.168.255.3 | PASS | - |
| 220 | leaf03-dc1 | Routing Table | Remote Lo0 address | 192.168.255.4 | PASS | - |
| 221 | leaf03-dc1 | Routing Table | Remote Lo0 address | 192.168.255.5 | PASS | - |
| 222 | leaf03-dc1 | Routing Table | Remote Lo0 address | 192.168.255.6 | PASS | - |
| 223 | leaf04-dc1 | Routing Table | Remote Lo0 address | 192.168.255.3 | PASS | - |
| 224 | leaf04-dc1 | Routing Table | Remote Lo0 address | 192.168.255.4 | PASS | - |
| 225 | leaf04-dc1 | Routing Table | Remote Lo0 address | 192.168.255.5 | PASS | - |
| 226 | leaf04-dc1 | Routing Table | Remote Lo0 address | 192.168.255.6 | PASS | - |
| 227 | spine01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.3 | PASS | - |
| 228 | spine01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.4 | PASS | - |
| 229 | spine01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.5 | PASS | - |
| 230 | spine01-dc1 | Routing Table | Remote Lo0 address | 192.168.255.6 | PASS | - |
| 231 | spine02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.3 | PASS | - |
| 232 | spine02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.4 | PASS | - |
| 233 | spine02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.5 | PASS | - |
| 234 | spine02-dc1 | Routing Table | Remote Lo0 address | 192.168.255.6 | PASS | - |
| 235 | leaf01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf01-dc1 - 192.168.255.3 Destination: 192.168.255.3 | PASS | - |
| 236 | leaf01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf01-dc1 - 192.168.255.3 Destination: 192.168.255.4 | PASS | - |
| 237 | leaf01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf01-dc1 - 192.168.255.3 Destination: 192.168.255.5 | PASS | - |
| 238 | leaf01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf01-dc1 - 192.168.255.3 Destination: 192.168.255.6 | PASS | - |
| 239 | leaf02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf02-dc1 - 192.168.255.4 Destination: 192.168.255.3 | PASS | - |
| 240 | leaf02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf02-dc1 - 192.168.255.4 Destination: 192.168.255.4 | PASS | - |
| 241 | leaf02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf02-dc1 - 192.168.255.4 Destination: 192.168.255.5 | PASS | - |
| 242 | leaf02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf02-dc1 - 192.168.255.4 Destination: 192.168.255.6 | PASS | - |
| 243 | leaf03-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf03-dc1 - 192.168.255.5 Destination: 192.168.255.3 | PASS | - |
| 244 | leaf03-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf03-dc1 - 192.168.255.5 Destination: 192.168.255.4 | PASS | - |
| 245 | leaf03-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf03-dc1 - 192.168.255.5 Destination: 192.168.255.5 | PASS | - |
| 246 | leaf03-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf03-dc1 - 192.168.255.5 Destination: 192.168.255.6 | PASS | - |
| 247 | leaf04-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf04-dc1 - 192.168.255.6 Destination: 192.168.255.3 | PASS | - |
| 248 | leaf04-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf04-dc1 - 192.168.255.6 Destination: 192.168.255.4 | PASS | - |
| 249 | leaf04-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf04-dc1 - 192.168.255.6 Destination: 192.168.255.5 | PASS | - |
| 250 | leaf04-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: leaf04-dc1 - 192.168.255.6 Destination: 192.168.255.6 | PASS | - |
| 251 | spine01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine01-dc1 - 192.168.255.1 Destination: 192.168.255.3 | PASS | - |
| 252 | spine01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine01-dc1 - 192.168.255.1 Destination: 192.168.255.4 | PASS | - |
| 253 | spine01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine01-dc1 - 192.168.255.1 Destination: 192.168.255.5 | PASS | - |
| 254 | spine01-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine01-dc1 - 192.168.255.1 Destination: 192.168.255.6 | PASS | - |
| 255 | spine02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine02-dc1 - 192.168.255.2 Destination: 192.168.255.3 | PASS | - |
| 256 | spine02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine02-dc1 - 192.168.255.2 Destination: 192.168.255.4 | PASS | - |
| 257 | spine02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine02-dc1 - 192.168.255.2 Destination: 192.168.255.5 | PASS | - |
| 258 | spine02-dc1 | Loopback0 Reachability | Loopback0 Reachability | Source: spine02-dc1 - 192.168.255.2 Destination: 192.168.255.6 | PASS | - |
