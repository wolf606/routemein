from Library.BinaryNumbersLib import binaryNumbersHandler as bnh
from Library.IPv4Lib import IPv4
from Library.Models.Device import Device

class Network:

    types = ('WAN', 'LAN', 'VLAN')

    def __init__(self, type: int, hosts: int) -> None:
        """Creation of a Network object.

        A Network object has: 
            - type attribute that can either be WAN or LAN.
            - hosts attribute that stores the max number of hosts 
            inside the Network
            - network_ip attribute that stores the Network ip.
            - mask attribute that stores the Network mask.
            - devices list that stores the devices connected
            to the Network as a tuple of (devices, ip)

        Parameters
        ----------
        type : int
            Network class ha a tuple of ('WAN', 'LAN', 'VLAN')
            use index 0 or 1 for selecting the Network type.
        hosts : int
            the max number of hosts inside the Network
        """
        self.type = Network.types[type]
        self.hosts = hosts
        self.network_ip = None
        self.mask = None
        #We save tuples of (device, ip) inside of the devices list.
        self.devices = []

    def connected_devices(self) -> str:
        if not len(self.devices) == 0:
            res = '\nConnected devices: \n'
            for dev in self.devices:
                res = res + dev[0].type+' '+str(dev[0].name)+' with IP '+str(dev[1])+'\n'
            return res
        return ''

    def __str__(self) -> str:
        return self.type+'\n'+'Hosts: '+str(self.hosts)+'\n'+'Network Address: '+str(self.network_ip)+'\n'+'Mask: '+str(self.mask)+self.connected_devices()
    
    def calculate_new_device_ip(self) -> IPv4:
        """When adding a device, we handle the IP assignation here.

        If there are no devices we start from the network_ip, however
        #if there are devices inside the Network, use the IP from the last
        device inside the devices list.

        Raises
        ------
        ValueError
            If devices list is empty and network_ip is None.
        """
        if len(self.devices) == 0:
            if not self.network_ip == None:
                #Converts the network_ip in binary and we add 1 to that ip with 
                #the binary numbers handler. Then we use the IPv4 function
                #to create a new IPv4 object from the result of the sum.
                return IPv4.create_new_ip_from_string(bnh.sum(self.network_ip.get_binary_string(), '1'))
            else: raise ValueError('RmiNetworkLib: network_ip is None. cant create ip with calculate_new_device_ip()')
        else:
            #Get the last device on the devices list and get its IP
            #Since we save devices as a tuple of (device, ip), 
            #we need to access the index 1 of the tuple
            #to get the IP.
            last_ip = self.devices[len(self.devices)-1][1]
            return IPv4.create_new_ip_from_string(bnh.sum(last_ip.get_binary_string(), '1'))

    def add_device(self, device: Device) -> None:
        """We handle the connection of devices to the Network here

        Calculate a new IP and add it to the devices list

        Parameters
        ----------
        device : device
            The device that needs to be added to the Network.

        Raises
        ------
        ValueError
            If device is None.
        """
        if not device == None:
            new_ip = self.calculate_new_device_ip()
            if not new_ip == None: self.devices.append((device, new_ip ))
            else: raise ValueError("RmiNetworkLib: add_device() new_ip as None type")
        else: raise ValueError("RmiNetworkLib: add_device() received device argument as None type")
    
    def get_device_ip(self, name: str) -> str:
        """Get the IP of a particular device in the Network.
        When traversing the Networks of a device, you need the IP
        of the device inside that Network. Since the IP it's saved
        inside the Network as a tuple (device, ip) in the devices list
        it's necessary to find the device that matches the name of the
        one we're interested.

        Parameters
        ----------
        name : str
            The name of the device.

        Raises
        ------
        LookupError
            If no matches are found inside the devices list.
        """
        for dev in self.devices:
            if dev[0].name == name:
                return str(dev[1])
        raise LookupError('RmiNetworkLib: device does not exist in Network devices list')

    def get_network_ip_str(self) -> str:
        """Get the Network IP of the Network object 

        Raises
        ------
        ValueError
            If network_ip is None.
        """
        if not self.network_ip == None: return str(self.network_ip)
        else: raise ValueError("RmiNetworkLib: network_ip is None type")

    def get_mask_str(self) -> str:
        """Get the Mask of the Network object 

        Raises
        ------
        ValueError
            If mask is None.
        """
        if not self.mask == None: return str(self.mask)
        else: raise ValueError("RmiNetworkLib: mask is None type")