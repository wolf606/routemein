import random
from Library.QuickSortLib import quicksort as qs
from Library.Models.IPv4Lib import IPv4
from Library.BinaryNumbersLib import binaryNumbersHandler as bnh

class addressing:

    #IP templates for each class
    ip_class_template = {
        'A': IPv4(random.randrange(0,127), 0, 0, 0),
        'B': IPv4(random.randrange(128,191), random.randrange(0,255), 0, 0),
        'C': IPv4(random.randrange(192,223), random.randrange(0,255), random.randrange(0,255), 0),
    }

    ip_class_hosts = {
        'A': 16777216,
        'B': 65536,
        'C': 256,
    }

    @staticmethod
    def set_first_ip(networks: list) -> int:
        """Selects the first IP for the first network in the list.

        This is where the addressing starts.

        Parameters
        ----------
        networks : list
            The list filled with networks.

        """
        networks = qs.sort(networks)
        max_hosts = networks[0].hosts
        ip_class = addressing.select_ip_class(max_hosts)
        networks[0].network_ip = addressing.ip_class_template.get(ip_class)
        reserved_bits = addressing.calculate_reserved_bits(networks[0].hosts)
        networks[0].mask = addressing.create_network_mask_reserved_bits(reserved_bits)
        return reserved_bits

    @staticmethod
    def select_ip_class(max_hosts: int) -> str:
        """Returns a character representing the IP class
        given a number of maximum hosts.

        Parameters
        ----------
        max_hosts : int
            The number of hosts of a network.

        """
        class_hosts = addressing.ip_class_hosts
        if max_hosts > class_hosts.get('B')-2:
            return 'A'
        elif max_hosts > class_hosts.get('C')-2 and max_hosts < class_hosts.get('B')-1:
            return 'B'
        elif max_hosts > 0 and max_hosts < class_hosts.get('C')-1:
            return 'C'

    @staticmethod
    def address_list(networks: list) -> None:
        """Handles the addressing of the networks inside a list.

        The list must contain network objects.

        Parameters
        ----------
        networks : list
            The list filled with networks.

        """
        reserved_bits = addressing.set_first_ip(networks)
        for i in range(1,len(networks)):
            prev_ip = networks[i-1].network_ip.get_binary_string()
            new_ip = bnh.sum(prev_ip,'1'+bnh.zeros[:reserved_bits])
            networks[i].network_ip = IPv4.create_new_ip_from_string(new_ip)
            reserved_bits = addressing.calculate_reserved_bits(networks[i].hosts)
            networks[i].mask = addressing.create_network_mask_reserved_bits(reserved_bits)

    @staticmethod
    def calculate_reserved_bits(hosts: int) -> int:
        """Returns the number of reserved bits of an IP given a number of hosts.

        Parameters
        ----------
        hosts : int
            The number of hosts of a network.

        Raises
        ------
        ValueError
            if the number of reserved bits exceeds the number 24.
        """
        for n in range(2,25):
            result = pow(2,n)-2
            if result >= hosts:
                return n
        raise ValueError('RmiAddressingLib: Number of hosts is just too high.')
    
    @staticmethod
    def create_network_mask_reserved_bits(reserved_bits: int):
        """Returns an IPv4 object that holds a mask ip made 
        from the reserved bits.

        Parameters
        ----------
        reserved_bits : int
            The number of reserved bits.
        """
        mask_num = 32-reserved_bits
        return IPv4.create_new_ip_from_string(bnh.ones[:mask_num]+bnh.zeros[:reserved_bits])