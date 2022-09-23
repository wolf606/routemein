from cgi import print_arguments
import string
from webbrowser import get


from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh

class IPv4:
    def __init__(self, oct1: int, oct2: int, oct3: int, oct4: int, mask: int = 8):
        self.ipV4 = [oct1, oct2, oct3, oct4]
        self.mask = mask
        self.check_ip()

    def __str__(self) -> string:
        return str(self.ipV4[0])+'.'+str(self.ipV4[1])+'.'+str(self.ipV4[2])+'.'+str(self.ipV4[3])


    """ verifica si la ip es de tipo int y si es mayor que 0 y menor que 255 """
    def check_ip(self) -> None:
        error = 'RmiIPv4Lib: Invalid value for IP at octet '
        if (self.ipV4[0] > 255 or self.ipV4[0] < 0) or (not isinstance(self.ipV4[0], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[0]))
        elif (self.ipV4[1] > 255 or self.ipV4[1] < 0) or (not isinstance(self.ipV4[1], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[1]))
        elif (self.ipV4[2] > 255 or self.ipV4[2] < 0) or (not isinstance(self.ipV4[2], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[2]))
        elif (self.ipV4[3] > 255 or self.ipV4[3] < 0) or (not isinstance(self.ipV4[3], int)):
            raise ValueError(error+'1. Value: '+str(self.ipV4[3]))


    """ retorna la ip en formato binario """
    def get_binary_string(self) -> string:
        return bnh.int_to_bin(self.ipV4[0])+bnh.int_to_bin(self.ipV4[1])+bnh.int_to_bin(self.ipV4[2])+bnh.int_to_bin(self.ipV4[3])


    """ cambia el valor de la ip a la siguiente ip ingresada
        recuerda que binary_number es un objeto de la clase binaryNumber que permite convertir un string a binari, tomando en cuenta los 8 primeros digitos del string
    """
    def set_ip_value_binary_str(self, binary_str: string) -> None:
        if not len(binary_str) == 32:
            raise ValueError('RmiIPv4Lib: String arr length is not exactly 32. Length: '+str(len(binary_str)))
        else:
            IPv4(int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2))
            self.ipV4[0], self.ipV4[1], self.ipV4[2], self.ipV4[3] = int(binary_str[:8], 2), int(binary_str[8:16], 2), int(binary_str[16:24], 2), int(binary_str[24:32], 2)


    def wildcard(self) -> string:
        ip = ''
        limit =  self.mask//8 
        for i in range(self.ipV4.__len__()):
            if i == limit:
                ip += str(2**(8-(self.mask - 8*i ))-1)
            elif i<limit:
                ip += '0'
            else:
                ip += '255'  
                    
            if i < 3:
                ip += '.'  
        return ip
    
            
        
    def getMaskIp(self) -> string:
        ip = ''
        limit =  self.mask//8 
        for i in range(self.ipV4.__len__()):
            if i == limit:
                ip += str(256-self.getHosts())
            elif i<limit:
                ip += '255'
            else:
                ip += '0'  
                    
            if i < 3:
                ip += '.'  
        return ip
    
    
    """el incremento es para saber cuantas subclases aumentamos desde la ip con su mascara  """
    def increaseSubclass(self, increase: int):
        
        auxIp = IPv4(self.ipV4[0], self.ipV4[1], self.ipV4[2], self.ipV4[3], self.mask)
        limit = self.mask//8
        for i in range(increase):
            auxIp.ipV4[limit] = bnh.addEspecificOne(auxIp.ipV4[limit],(self.mask - 8*limit))
        return auxIp
    
        

    def getHosts(self) -> int:
        return 2**(32-self.mask)
    
    def getRed(self) -> string:
        return 2**(self.mask)
    
    
    
    def getClass(self) -> string: 
        if self.mask <= 255  and self.mask >= 0:
            return 'C'
        elif self.mask <= 65535 and self.mask >= 256:
            return 'B'
        elif self.mask <= 16777215 and self.mask >= 65536:
            return 'A'