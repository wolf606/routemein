from multiprocessing.connection import answer_challenge
from colorama import Fore
from colorama import Style

class userInputLib:

    @staticmethod
    def ask_int_data(input_text: str, separator: str) -> int:
        result = False
        num = 0
        while not result:
            try:
                num = int(input(input_text+separator+' '))
                result = True
            except ValueError:
                userInputLib.print_err('User input was not a number')
        return num

    @staticmethod
    def yes_or_no(text_input: str):
        result = False
        answer = ''
        while not result:
            answer = input(text_input).upper()
            if (answer == 'YES' or answer == 'Y') or (answer == 'NO' or answer == 'N'):
                result = True
            else: userInputLib.print_err('Use YES or NO')
        if answer == 'YES' or answer == 'Y': return True
        else: return False

    @staticmethod
    def print_err(text: str) -> None:
        print(f'{Fore.RED}'+text+Style.RESET_ALL)

    @staticmethod
    def print_warning(text: str) -> None:
        print(f'{Fore.YELLOW}'+text+Style.RESET_ALL)

    @staticmethod
    def print_blue(text: str) -> None:
        print(f'{Fore.BLUE}'+text+Style.RESET_ALL)

    @staticmethod
    def print_magenta(text: str) -> None:
        print(f'{Fore.MAGENTA}'+text+Style.RESET_ALL)

    @staticmethod
    def input_blue(text: str) -> str:
        return input(f'{Fore.BLUE}'+text+Style.RESET_ALL)

    @staticmethod
    def input_magenta(text: str) -> str:
        return input(f'{Fore.MAGENTA}'+text+Style.RESET_ALL)