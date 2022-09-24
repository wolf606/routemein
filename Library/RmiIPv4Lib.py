from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh

class IPv4:
    
    def __init__(self, oct1: int, oct2: int, oct3: int, oct4: int) -> None:
        """Creates an IPv4 object.

        octet1, octet2, octet3, octet4 represents the octets of an IP
        as integers.

        Parameters
        ----------
        octet1 : int
            The integer value of the first octet.
        octet2 : int
            The integer value of the second octet.
        octet3 : int
            The integer value of the third octet.
        octet4 : int
            The integer value of the fourth octet.

        Raises
        ------
        ValueError
            If the value of any octet is out of range.
            [0-255]
        """
        self.oct1 = oct1
        self.oct2 = oct2
        self.oct3 = oct3
        self.oct4 = oct4
        self.check_ip()

    def __str__(self) -> str:
        """Returns the IP object in a string with the format 'X.X.X.X'.

        """
        return str(self.oct1)+'.'+str(self.oct2)+'.'+str(self.oct3)+'.'+str(self.oct4)

    def get_ip_class(self) -> str:
        """Returns as a character the class of the IP object

        """
        if self.oct1 >= 0 and self.oct1 <= 127: return 'A'
        elif self.oct1 >= 128 and self.oct1 <= 191: return 'B'
        elif self.oct1 >= 192 and self.oct1 <= 223: return 'C'

    def check_ip(self) -> None:
        """Checks if the object IP is a valid one (octet by octet), else raise an exception

        Raises
        ------
        ValueError
            If an octet is out of range. [0-255]
        """
        error = 'RmiIPv4Lib: Invalid value for IP at octet '
        if (self.oct1 > 255 or self.oct1 < 0) or (not isinstance(self.oct1, int)):
            raise ValueError(error+'1. Value: '+str(self.oct1))
        elif (self.oct2 > 255 or self.oct2 < 0) or (not isinstance(self.oct2, int)):
            raise ValueError(error+'2. Value: '+str(self.oct2))
        elif (self.oct3 > 255 or self.oct3 < 0) or (not isinstance(self.oct3, int)):
            raise ValueError(error+'3. Value: '+str(self.oct3))
        elif (self.oct4 > 255 or self.oct4 < 0) or (not isinstance(self.oct4, int)):
            raise ValueError(error+'4. Value: '+str(self.oct4))

    def get_binary_string(self) -> str:
        """Returns the full IP in binary as a string

        """
        return bnh.int_to_bin(self.oct1)+bnh.int_to_bin(self.oct2)+bnh.int_to_bin(self.oct3)+bnh.int_to_bin(self.oct4)
    
    def set_ip_value_binary_str(self, binary_str: str) -> None:
        """Sets the value of the IP object (octet by octet) when it receives an IP in binary as a string

        Parameters
        ----------
        binary_str : str
            The IP in binary.

        """
        if not len(binary_str) == 32:
            raise ValueError('RmiIPv4Lib: String arr length is not exactly 32. Length: '+str(len(binary_str)))
        else:
            #We need to check the ip is valid before setting the values inside the object
            #The IPv4 constructor method already handles the IP validation so we use that instead
            #Slice the string octet by octet and convers it to integers as the IPv4 constructor only receives integers
            IPv4(int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2))
            #if the IP is valid an exception is raised, else we set the values of the octets with the ones of the binary_str
            self.oct1, self.oct2, self.oct3, self.oct4 = int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2)
    
    @staticmethod
    def create_new_ip_from_string(binary_str: str):
        """Creates an IP object from a string of an IP in binary.

        Parameters
        ----------
        binary_str : str
            The IP in binary.
        """
        return IPv4(int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2))

    @staticmethod
    def get_ip_class_from_string(binary_str: str) -> str:
        """Returns as a character the class of an IP that is in binary.

        Parameters
        ----------
        binary_str : str
            The IP in binary.
        """
        oct1 = int(binary_str[:8], 2)
        if oct1 >= 0 and oct1 <= 127: return 'A'
        elif oct1 >= 128 and oct1 <= 191: return 'B'
        elif oct1 >= 192 and oct1 <= 223: return 'C'