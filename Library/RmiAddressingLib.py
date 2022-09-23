import imp
import string

from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.RmiIPv4Lib import IPv4 as ip

class addressingHandler:

    @staticmethod
    def addressing(list, initialIp: ip) :
        list =  sorted(list, reverse=True)
        addresingIP = []   
        
        ipAux = initialIp

        for i in range(len(list)):        
            ipAux.mask = addressingHandler.findMask(list[i])
            addresingIP.append(ipAux)
            ipAux = ip()
        return ip
      
        
    @staticmethod
    def findMask(number: int) -> int:
        mask = 1
        for i in range(1, 24):
            if number < 2**i:
                mask = i-32
                break
        return mask
    
   