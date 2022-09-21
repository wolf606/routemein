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