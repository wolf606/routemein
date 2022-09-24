class binaryNumbersHandler:
    
    ones='11111111111111111111111111111111'
    zeros='00000000000000000000000000000000'

    @staticmethod
    def sum(num1: str, num2: str) -> str:
        """Adds two numbers in binary.

        Parameters
        ----------
        num1 : str
            The number in binary as a string.
            
        num2 : str
            The number in binary as a string.
        """
        return binaryNumbersHandler.int_to_bin(int(num1,2)+int(num2,2))

    @staticmethod
    def int_to_bin(num: int) -> str:
        """Converts a number in integer to binary.

        Parameters
        ----------
        num : int
            The number as an integer.

        """
        res = bin(num)[2:]
        if len(res) < 8:
            res=binaryNumbersHandler.zeros[:8-len(res)]+res
        elif len(res) < 32 and len(res) > 8:
            res=binaryNumbersHandler.zeros[:32-len(res)]+res
        return res