import os
from Library.Controllers.NetworkController import NetworkController
from Library.Controllers.DeviceController import DeviceController
from Library.UserInputLib import userInputLib as userin
from Library.Views.DeviceView import DeviceView

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class NetworkView:
    def __init__(self) -> None:
        self.net_con = NetworkController()

    def add_wans(self):
        clear()
        net = 'WANS'
        userin.print_blue('||||||||||||||||||| CREATE '+net+' |||||||||||||||')
        tabs = '    '
        update = False
        num = userin.ask_int_data('How many '+net+' are we setting up?', ' =')
        i = 0
        while i < num:
            clear()
            userin.print_blue(tabs+net[:len(net)-1]+' '+str(i))
            hosts = userin.ask_int_data(tabs+'How many hosts will there be in?',' =')
            if update: self.net_con.update_wan(i, hosts)
            else: self.net_con.store_wan(hosts)
            update = userin.yes_or_no(tabs+'Do you want to change the number of hosts? ')
            if update: i = i-1
            i = i+1
        self.net_con.address_wan()
        self.list_wans()

    def list_wans(self):
        clear()
        userin.print_blue('||||||||||||||||||| LIST WANS |||||||||||||||')
        wans = self.net_con.index_wan()
        i = 0
        for n in wans:
            print('\n'+str(i)+' '+str(n))
            i = i+1
        input('\nPress any key to continue')

    def add_lans(self):
        clear()
        net = 'LANS'
        userin.print_magenta('||||||||||||||||||| CREATE '+net+' |||||||||||||||')
        tabs = '    '
        update = False
        num = userin.ask_int_data('How many '+net+' are we setting up?', ' =')
        i = 0
        while i < num:
            clear()
            userin.print_magenta(tabs+net[:len(net)-1]+' '+str(i))
            hosts = userin.ask_int_data(tabs+'How many hosts will there be in?',' =')
            if update: self.net_con.update_lan(i, hosts)
            else: self.net_con.store_lan(hosts)
            update = userin.yes_or_no(tabs+'Do you want to change the number of hosts? ')
            if update: i = i-1
            i = i+1
        self.net_con.address_lan()
        self.list_lans()

    def list_lans(self):
        clear()
        userin.print_magenta('||||||||||||||||||| LIST WANS |||||||||||||||')
        lans = self.net_con.index_lan()
        i = 0
        for n in lans:
            print('\n'+str(i)+' '+str(n))
            i = i+1
        input('\nPress any key to continue')

    def is_wans_empty(self):
        return len(self.net_con.index_wan()) == 0

    def add_routers_to_wan(self, dev_con: DeviceController):
        clear()
        net = 'WANS'
        userin.print_magenta('||||||||||||||||||| ADD DEVICES TO '+net+' |||||||||||||||')

        dev_v = DeviceView()
        dev_v.dev_con = dev_con
        wan_index = 0
        for net in self.net_con.index_wan():
            clear()
            wan_devs = []
            for o in range(2):
                while True:
                    clear()
                    dev_v.list_routers()
                    userin.print_magenta('Selected WAN')
                    print(str(net))
                    num = userin.ask_int_data('Routers selected: '+str(wan_devs)+'\n Select a router (MAX 2)', ':')
                    if (not dev_con.get_router(num) == None) and wan_devs.count(num) == 0: wan_devs.append(num); break
                    else: userin.print_err('WRONG ROUTER INDEX'); input('Press any key to try again')
            for dev_index in wan_devs: 
                dev_con.add_wan_to_router(dev_index, net)
                self.net_con.add_router_to_wan(dev_con.get_router(dev_index), wan_index)
            wan_index = wan_index+1
        self.list_wans()
