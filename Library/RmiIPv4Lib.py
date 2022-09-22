import string
from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh

class IPv4:
    def __init__(self, oct1: int, oct2: int, oct3: int, oct4: int):
        self.oct1 = oct1
        self.oct2 = oct2
        self.oct3 = oct3
        self.oct4 = oct4
        self.check_ip()

    def __str__(self) -> string:
        return str(self.oct1)+'.'+str(self.oct2)+'.'+str(self.oct3)+'.'+str(self.oct4)

    def check_ip(self) -> None:
        error = 'RmiIPv4Lib: Invalid value for IP at octet '
        if (self.oct1 > 255 or self.oct1 < 0) or (not isinstance(self.oct1, int)):
            raise ValueError(error+'1. Value: '+str(self.oct1))
        elif (self.oct2 > 255 or self.oct2 < 0) or (not isinstance(self.oct2, int)):
            raise ValueError(error+'2. Value: '+str(self.oct2))
        elif (self.oct3 > 255 or self.oct3 < 0) or (not isinstance(self.oct3, int)):
            raise ValueError(error+'3. Value: '+str(self.oct3))
        elif (self.oct4 > 255 or self.oct4 < 0) or (not isinstance(self.oct4, int)):
            raise ValueError(error+'4. Value: '+str(self.oct4))

    def get_binary_string(self) -> string:
        return bnh.int_to_bin(self.oct1)+bnh.int_to_bin(self.oct2)+bnh.int_to_bin(self.oct3)+bnh.int_to_bin(self.oct4)

    def set_ip_value_binary_str(self, binary_str: string) -> None:
        if not len(binary_str) == 32:
            raise ValueError('RmiIPv4Lib: String arr length is not exactly 32. Length: '+str(len(binary_str)))
        else:
            IPv4(int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2))
            self.oct1, self.oct2, self.oct3, self.oct4 = int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2)

