import imp
import string

class binaryNumbersHandler:
    zeros='00000000'

    @staticmethod
    def sum(num1: string, num2: string) -> string:
        return binaryNumbersHandler.int_to_bin(int(num1,2)+int(num2,2))

    @staticmethod
    def int_to_bin(num: int) -> string:
        res = bin(num)[2:]
        if len(res) < 8:
            res=binaryNumbersHandler.zeros[0:8-len(res)]+res
        return res
    
    @staticmethod
    def bin_to_int(bin: string) -> int:
        return int(bin, 2)
    
    @staticmethod
    def add_ones_to_the_right(ditance) -> string:
        oct = ""
        for i in range(8):
            if i < ditance:
                oct += '1'
            else:
                oct += '0'
        return binaryNumbersHandler.bin_to_int(oct)
    
    
    
    @staticmethod
    def addEspecificOne(octect: int, pos: int):
        pos = pos-1
        strBin = list(binaryNumbersHandler.int_to_bin(octect)) 
        if pos >= 8 or pos < 0:
             raise ValueError('RmiBinaryNumbersLib: there is no more space to add a new one inside the octect: ') 
        if strBin[pos] == '0':
            strBin[pos] = '1'   
            return binaryNumbersHandler.bin_to_int("".join(strBin))
        elif strBin[pos] == '1':
            strBin[pos] = '0'
       
            return binaryNumbersHandler.addEspecificOne(binaryNumbersHandler.bin_to_int("".join(strBin)), pos)
            
