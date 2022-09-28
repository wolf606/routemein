class Device:
    
    port = '0/0'

    types = ('Router', 'PC', 'Switch')

    def __init__(self, type: int, name: str) -> None:
        """Creates a Device object.

        This Device can be a router, a PC or a switch.

        types = {
        0: 'Router',
        1: 'PC',
        2: 'Switch',
        }

        Parameters
        ----------
        name : str
            The name of the Device.

        Raises
        ------
        NotImplementedError
            If the Device name is empty.
        """
        self.type = Device.types[type]
        if not name == '': self.name = name
        else: raise ValueError('RmiDeviceLib: Device name cannot be empty.')
        #we add networks inside fastethernet interface only
        self.fe = []
        #networks inside serial interface only
        self.serial = []

    def serial_str(self) -> str:
        if not len(self.serial) == 0:
            res = '\nSerial connections to networks:\n'
            i = 0
            for c in self.serial:
                res = res + c.type + ' with Network IP ' + str(c.network_ip) + ' over port ' + self.get_interface_port(i) + '\n'
                i = i+1
            return res
        return ''

    def __str__(self) -> str:
        return self.type+'\n'+'Name: '+str(self.name)+self.serial_str()

    def get_interface_port(self, index: int) -> str:
        """Returns string of the port according to the index

        When traversing the list of fe or serial it comes in handy to print the port

        Parameters
        ----------
        index : int
            The index of the network inside the interface list.

        Raises
        ------
        TypeError
            if index is not an integer.
        """
        if isinstance(index, int):
            #slice port to get only the "0/" string and concatenates it to the index 
            return Device.port[:2]+str(index)
        else: raise TypeError('RmiDeviceLib: Expected int type for index as arg')
