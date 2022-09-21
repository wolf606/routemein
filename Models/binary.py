import string

class binary:
    zeros='00000000'
    digits=['0','1']
    def __init__(self):
        self.foo = None

    @staticmethod
    def sum(num1: string, num2: string) -> string:
        return binary.int_to_bin(int(num1,2)+int(num2,2))

    @staticmethod
    def int_to_bin(num: int) -> string:
        res = bin(num)[2:]
        if len(res) < 8:
            res=binary.zeros[0:8-len(res)]+res
        return res