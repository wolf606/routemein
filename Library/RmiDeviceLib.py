class device:
    
    port = '0/0'

    def __init__(self, name:str) -> None:
        """Creates a device object.

        This device can be a router or a PC.

        Parameters
        ----------
        name : str
            The name of the device.

        Raises
        ------
        NotImplementedError
            If the device name is empty.
        """
        if not name == '':
            self.name = name
        else: raise ValueError('RmiDeviceLib: device name cannot be empty.')
        #we add networks inside fastethernet interface only here
        self.fe = []
        #networks inside serial interface only
        self.serial = []

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
            return device.port[:2]+str(index)
        else: raise TypeError('RmiDeviceLib: Expected int type for index as arg')
