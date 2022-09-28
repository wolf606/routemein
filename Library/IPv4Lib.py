from Library.BinaryNumbersLib import binaryNumbersHandler as bnh

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
        IPv4.check_ip(oct1, oct2, oct3, oct4)
        self.oct1 = oct1
        self.oct2 = oct2
        self.oct3 = oct3
        self.oct4 = oct4

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

    @staticmethod
    def check_ip(oct1: int, oct2: int, oct3: int, oct4: int) -> None:
        """Checks if the object IP is a valid one (octet by octet), else raise an exception

        Parameters
        ----------
        oct1 : int
            The integer value of the first octet.
        oct2 : int
            The integer value of the second octet.
        oct3 : int
            The integer value of the third octet.
        oct4 : int
            The integer value of the fourth octet.

        Raises
        ------
        ValueError
            If an octet is out of range. [0-255]
        """
        IPv4.check_octet('1', oct1)
        IPv4.check_octet('2', oct2)
        IPv4.check_octet('3', oct3)
        IPv4.check_octet('4', oct4)

    @staticmethod
    def check_octet(octet_pos: str, octet_value: int) -> bool:
        """Checks if an octet is an integer and is within the range of [0,255]

        Raises
        ------
        ValueError
            If the octet is out of range. [0-255]
    """
        error = 'RmiIPv4Lib: Invalid value for IP at octet '+octet_pos
        if (not isinstance(octet_value, int)) or (octet_value > 255 or octet_value < 0):
            raise ValueError(error+'. Octet value: '+str(octet_value))

    def get_binary_string(self) -> str:
        """Returns the full IP in binary as a string

        """
        return bnh.int_to_bin(self.oct1)+bnh.int_to_bin(self.oct2)+bnh.int_to_bin(self.oct3)+bnh.int_to_bin(self.oct4)

    @staticmethod
    def check_ip_binary_str_length(binary_str: str):
        if not len(binary_str) == 32: raise ValueError('RmiIPv4Lib: String arr length is not exactly 32. Length: '+str(len(binary_str)))
    
    def set_ip_value_binary_str(self, binary_str: str) -> None:
        """Sets the value of the IP object (octet by octet) when it receives an IP in binary as a string

        Parameters
        ----------
        binary_str : str
            The IP in binary.

        """
        IPv4.check_ip_binary_str_length(binary_str)
        #We need to check the ip is valid before setting the values inside the object
        #The IPv4 constructor method already handles the IP validation so we use that instead
        #Slice the string octet by octet and convers it to integers as the IPv4 constructor only receives integers
        oct1, oct2, oct3, oct4 = int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2)
        IPv4.check_ip(oct1, oct2, oct3, oct4)
        #if the IP is NOT valid an exception is raised, else we set the values of the octets with the ones of the binary_str
        self.oct1, self.oct2, self.oct3, self.oct4 = oct1, oct2, oct3, oct4
    
    @staticmethod
    def create_new_ip_from_string(binary_str: str):
        """Creates an IP object from a string of an IP in binary.

        Parameters
        ----------
        binary_str : str
            The IP in binary.
        """
        IPv4.check_ip_binary_str_length(binary_str)
        return IPv4(int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2))