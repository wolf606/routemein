from Library.Models.Network import Network
from Library.AddressingLib import addressing

class NetworkController:

    def __init__(self) -> None:
        self.wan = []
        self.lan = []
        self.vlan = []

    def index_wan(self) -> list:
        return self.wan

    def index_lan(self) -> list:
        return self.lan

    def index_vlan(self) -> list:
        return self.vlan

    def get_wan(self, index: int) -> Network:
        try: return self.wan[index]
        except: return None

    def get_lan(self, index: int) -> Network:
        try: return self.lan[index]
        except: return None

    def get_vlan(self, index: int) -> Network:
        try: return self.vlan[index]
        except: return None

    def store_wan(self, hosts: int) -> Network:
        try: net = Network(0, hosts)
        except: return None
        self.wan.append(net)
        return net

    def store_lan(self, hosts: int) -> Network:
        try: net = Network(1, hosts)
        except: return None
        self.lan.append(net)
        return net

    def store_vlan(self, hosts: int) -> Network:
        try: net = Network(2, hosts)
        except: return None
        self.vlan.append(net)
        return net

    def update_wan(self, index: int, hosts: int) -> Network:
        try: net = Network(0, hosts)
        except: return None
        self.wan.insert(index, net)
        self.wan.pop(index+1)
        return self.wan[index]

    def update_lan(self, index: int, hosts: int) -> Network:
        try: net = Network(1, hosts)
        except: return None
        self.lan.insert(index, net)
        self.lan.pop(index+1)
        return self.lan[index]

    def update_vlan(self, index: int, hosts: int) -> Network:
        try: net = Network(2, hosts)
        except: return None
        self.vlan.insert(index, net)
        self.vlan.pop(index+1)
        return self.vlan[index]

    def delete_wan(self, index: int) -> Network:
        try: return self.wan.pop(index)
        except: return None

    def delete_lan(self, index: int) -> Network:
        try: return self.lan.pop(index)
        except: return None

    def delete_vlan(self, index: int) -> Network:
        try: return self.vlan.pop(index)
        except: return None

    def address_wan(self) -> None:
        addressing.address_list(self.wan)

    def address_lan(self) -> None:
        addressing.address_list(self.lan)

    def add_router_to_wan(self, device, lan_index: int):
        self.wan[lan_index].add_device(device)
