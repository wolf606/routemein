from operator import index
from Library.Models.Device import Device

class DeviceController:
    def __init__(self) -> None:
        self.router = []
        self.pc = []
        self.switch = []

    def index_router(self) -> list:
        return self.router

    def index_pc(self) -> list:
        return self.pc

    def index_switch(self) -> list:
        return self.switch

    def get_router(self, index: int) -> Device:
        try: return self.router[index]
        except: return None

    def get_pc(self, index: int) -> Device:
        try: return self.pc[index]
        except: return None

    def get_switch(self, index: int) -> Device:
        try: return self.switch[index]
        except: return None

    def store_router(self, name: str) -> Device:
        try: dev = Device(0, name)
        except: return None
        self.router.append(dev)
        return dev

    def store_pc(self, name: str) -> Device:
        try: dev = Device(1, name)
        except: return None
        self.pc.append(dev)
        return dev

    def store_switch(self, name: str) -> Device:
        try: dev = Device(2, name)
        except: return None
        self.switch.append(dev)
        return dev

    def update_router(self, index: int, name: str) -> Device:
        try: dev = Device(0, name)
        except: return None
        self.router.insert(index, dev)
        self.router.pop(index+1)
        return self.router[index]

    def update_pc(self, index: int, name: str) -> Device:
        try: dev = Device(1, name)
        except: return None
        self.pc.insert(index, dev)
        self.pc.pop(index+1)
        return self.pc[index]

    def update_switch(self, index: int, name: str) -> Device:
        try: dev = Device(2, name)
        except: return None
        self.switch.insert(index, dev)
        self.switch.pop(index+1)
        return self.switch[index]

    def delete_router(self, index: int) -> Device:
        try: return self.router.pop(index)
        except: return None

    def delete_pc(self, index: int) -> Device:
        try: return self.pc.pop(index)
        except: return None

    def delete_switch(self, index: int) -> Device:
        try: return self.switch.pop(index)
        except: return None

    def add_wan_to_router(self, dev_index: int, network) -> None:
        self.router[dev_index].serial.append(network)