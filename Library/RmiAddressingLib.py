import random
from Library.RmiNetworkLib import network
from Library.RmiQuickSortLib import quicksort as qs
from Library.RmiIPv4Lib import IPv4
from Library.RmiBinaryNumbersLib import binaryNumbersHandler as bnh

class addressing:

    #IP templates for each class
    ips = {
        'A': IPv4(random.randrange(0,127), 0, 0, 0),
        'B': IPv4(random.randrange(128,191), random.randrange(0,255), 0, 0),
        'C': IPv4(random.randrange(192,223), random.randrange(0,255), random.randrange(0,255), 0),
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
        networks[0].network_ip = addressing.ips.get(ip_class)
        reserved_bits = addressing.calculate_reserved_bits(networks[0].hosts)
        networks[0].mask = network.create_network_mask_reserved_bits(reserved_bits)
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
        if max_hosts > 65534:
            return 'A'
        elif max_hosts > 254 and max_hosts < 65535:
            return 'B'
        elif max_hosts > 0 and max_hosts < 255:
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
            networks[i].mask = network.create_network_mask_reserved_bits(reserved_bits)

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
    