from colorama import Fore
from colorama import Style

from Library.BinaryNumbersLib import binaryNumbersHandler as bnh
from Library.Models.IPv4Lib import IPv4 as ip
from Library.Models.Device import device
from Library.Models.Network import network
from Library.AddressingLib import addressing

def main():
    bin_num_lib_tests(5)
    ipv4_lib_tests(6)

def bin_num_lib_tests(test: int) -> None:
    print(f'{Fore.MAGENTA}BinaryNumbersLib handler test{Style.RESET_ALL}')
    if test == 0:
        print(f'{Fore.BLUE}- BinaryNumbersLib int_to_bin:{Style.RESET_ALL}')
        for i in range(257):
            conv = bin(int(bnh.int_to_bin(i), 2))
            print('Integer: '+str(i)+' -> Binary: '+conv, end='')
            if bin(i) == conv: print(' true')
            else: raise ValueError(f'{Fore.RED}Error in bnh.int_to_bin(){Style.RESET_ALL}')
    elif test == 1:
        print(f'{Fore.BLUE}- BinaryNumbersLib sum:{Style.RESET_ALL}')
        for i in range(300):
            num = bnh.int_to_bin(i)
            res = bin(int(bnh.sum(num, num), 2))
            print(num+' + '+num+' = '+res, end='')
            if bin(i+i) == res: print(' true')
            else: raise ValueError(f'{Fore.RED}Error in bnh.sum(){Style.RESET_ALL}')

        for i in range(300):
            num = bnh.int_to_bin(i)
            num1 = bnh.int_to_bin(i+100)
            res = bin(int(bnh.sum(num1, num), 2))
            print(num1+' + '+num+' = '+res, end='')
            if bin(i+(i+100)) == res: print(' true')
            else: raise ValueError(f'{Fore.RED}Error in bnh.sum(){Style.RESET_ALL}')
    else: print(f'{Fore.RED} TEST '+str(test)+' DOES NOT EXISTS'+Style.RESET_ALL)


def ipv4_lib_tests(test: int) -> None:
    print(f'{Fore.MAGENTA}BinaryNumbersLib handler test{Style.RESET_ALL}')
    if test == 0:
        print(f'{Fore.BLUE}- IPv4Lib ip constructor:{Style.RESET_ALL}')
        for i in range(-1,257):
            try:
                print(str(ip(i, i, i, i))+' is good')
            except ValueError:
                print(f'{Fore.YELLOW}IP '+str(i)+'.'+str(i)+'.'+str(i)+'.'+str(i)+' was handled'+Style.RESET_ALL)

        i = 3.14
        try:
            print(str(ip(i, i, i, i))+' is good')
            raise ValueError(f'{Fore.RED}Octets must be integers. Value: '+str(i)+Style.RESET_ALL)
        except ValueError:
            print(f'{Fore.YELLOW}IP '+str(i)+'.'+str(i)+'.'+str(i)+'.'+str(i)+' was handled'+Style.RESET_ALL)
        
        i = '4a'
        try:
            print(str(ip(i, i, i, i))+' is good')
            raise ValueError(f'{Fore.RED}Octets must be integers. Value: '+str(i)+Style.RESET_ALL)
        except ValueError:
            print(f'{Fore.YELLOW}IP '+str(i)+'.'+str(i)+'.'+str(i)+'.'+str(i)+' was handled'+Style.RESET_ALL)
    elif test == 1:
        print(f'{Fore.BLUE}- IPv4Lib ip get_binary_string():{Style.RESET_ALL}')
        for i in range(256):
            ip1 = ip(i, i, i, i)
            ip_bin = ip1.get_binary_string()
            try:
                ip.check_ip_binary_str_length(ip_bin)
                print(str(ip1)+' -> '+ip_bin+' good')
            except ValueError:
                print(f'{Fore.RED}IP '+str(ip1)+' is wrong'+Style.RESET_ALL)
    elif test == 2:
        print(f'{Fore.BLUE}- IPv4Lib ip set_ip_value_binary_str():{Style.RESET_ALL}')
        for i in range(-10, 257):
            ip1 = ip(1,2,3,4)
            o1, o2, o3, o4 = bnh.int_to_bin(i), bnh.int_to_bin(i), bnh.int_to_bin(i), bnh.int_to_bin(i)
            ip_bin = o1+o2+o3+o4
            try:
                ip1.set_ip_value_binary_str(ip_bin)
                print(str(i)+'.'+str(i)+'.'+str(i)+'.'+str(i)+' -> '+ip_bin+' good')
            except ValueError:
                print(f'{Fore.YELLOW}IP '+str(i)+'.'+str(i)+'.'+str(i)+'.'+str(i)+' was handled.'+Style.RESET_ALL)
    elif test == 3:
        print(f'{Fore.BLUE}- IPv4Lib ip create_new_ip_from_string():{Style.RESET_ALL}')
        for i in range(-10, 257):
            o1, o2, o3, o4 = bnh.int_to_bin(i), bnh.int_to_bin(i), bnh.int_to_bin(i), bnh.int_to_bin(i)
            ip_bin = o1+o2+o3+o4
            try:
                print(str(ip.create_new_ip_from_string(ip_bin))+' <- '+ip_bin+' good')
            except ValueError:
                print(f'{Fore.YELLOW}IP '+str(i)+'.'+str(i)+'.'+str(i)+'.'+str(i)+' was handled.'+Style.RESET_ALL)
    else: print(f'{Fore.RED} TEST '+str(test)+' DOES NOT EXISTS'+Style.RESET_ALL)

def print_err(text: str) -> str:
    print(f'{Fore.RED}'+text+Style.RESET_ALL)

def print_warning(text: str) -> str:
    print(f'{Fore.YELLOW}'+text+Style.RESET_ALL)

def print_blue(text: str) -> str:
    print(f'{Fore.BLUE}'+text+Style.RESET_ALL)

def print_magenta(text: str) -> str:
    print(f'{Fore.MAGENTA}'+text+Style.RESET_ALL)

if __name__ == "__main__":
    main() 
    router = device('Cisco 1')
    router1 = device('Cisco 2')
    host = device('Apple TV')

    wan = network(0, 4)
    lan = network(1, 200)

    wan.network_ip = ip(200, 10, 4, 24)
    wan.mask = ip(255, 255, 255, 248)

    print('wan ip: '+wan.get_network_ip_str())
    print('wan mask: '+wan.get_mask_str())

    wan.add_device(router)
    router.serial.append(wan)
    print('router ip: '+wan.get_device_ip('Cisco 1')+' in serial '+router.get_interface_port(0))
    wan.add_device(router1)
    router1.serial.append(wan)
    print('router ip: '+wan.get_device_ip('Cisco 2')+' in serial '+router1.get_interface_port(1))

    print(addressing.create_network_mask_reserved_bits(12))

    lan1 = network(1, 3850)
    lan2 = network(1, 1900)
    lan3 = network(1, 50)
    lan4 = network(1, 11)

    nets = [lan1,lan2,lan3,lan4]

    addressing.address_list(nets)

    i = 1
    for n in nets:
        print('net '+str(i)+' - ip: '+str(n.network_ip)+' | mask: '+str(n.mask))
        i=i+1

    print('\n')

    wan1 = network(0, 4)
    wan2 = network(0, 4)
    wan3 = network(0, 4)
    wan4 = network(0, 4)

    nets1 = [wan1,wan2,wan3,wan4]

    addressing.address_list(nets1)

    i = 1
    for n in nets1:
        print('net '+str(i)+' - ip: '+str(n.network_ip)+' | mask: '+str(n.mask))
        i=i+1