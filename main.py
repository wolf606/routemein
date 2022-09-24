from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh
from Library.RmiIPv4Lib import IPv4 as ip

print(bnh.int_to_bin(255))

print(bnh.sum('10000', '10000'))

for i in range(256):
    print(ip(i, i, i, i))

print(ip(254, 254, 254, 254).get_binary_string())
one = ip(254, 254, 254, 254)
one.set_ip_value_binary_str('11111100111111001111110011111100')
print(one)