import typing
from dataclasses import dataclass


@dataclass()
class Link:
    node_type: str
    node: str
    node_interface: str
    peer_type: str
    peer_node: str
    peer_interface: str

    def __str__(self):
        return (
            f"{self.node}-{self.node_interface}->{self.peer_node}-{self.peer_interface}"
        )


@dataclass
class P2PLink:
    type: str
    node: str
    node_interface: str
    leaf_ip_address: str
    peer_type: str
    peer_node: str
    peer_interface: str
    peer_ip_address: str

    def __str__(self):
        return f"{self.node}-{self.node_interface}:{self.leaf_ip_address}->{self.peer_node}-{self.peer_interface}:{self.peer_ip_address}"


def get_link(link_data: dict, link_type: str) -> typing.Union[Link, P2PLink]:
    if link_type == "p2p_link":
        return P2PLink(
            type=link_data["type"],
            node=link_data["node"],
            node_interface=link_data["node_interface"],
            leaf_ip_address=link_data["leaf_ip_address"],
            peer_type=link_data["peer_type"],
            peer_node=link_data["peer_node"],
            peer_interface=link_data["peer_interface"],
            peer_ip_address=link_data["peer_ip_address"],
        )
    elif link_type == "link":
        return Link(
            node_type=link_data["node_type"],
            node=link_data["node"],
            node_interface=link_data["node_interface"],
            peer_type=link_data["peer_type"],
            peer_node=link_data["peer_node"],
            peer_interface=link_data["peer_interface"],
        )
