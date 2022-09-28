import os
from Library.Controllers.DeviceController import DeviceController
from Library.UserInputLib import userInputLib as userin

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class DeviceView:
    def __init__(self) -> None:
        self.dev_con = DeviceController()

    def add_routers(self):
        clear()
        dev = 'ROUTERS'
        userin.print_blue('||||||||||||||||||| CREATE '+dev+' |||||||||||||||')
        tabs = '    '
        update = False
        num = userin.ask_int_data('How many '+dev+' are we setting up?', ' =')
        i = 0
        while i < num:
            clear()
            userin.print_blue(tabs+dev[:len(dev)-1]+' '+str(i))
            name = input(tabs+'Router name: ')
            if update: self.dev_con.update_router(i, name)
            else: self.dev_con.store_router(name)
            update = userin.yes_or_no(tabs+'Do you want to change the router name? ')
            if update: i = i-1
            i = i+1
        self.list_routers()

    def list_routers(self):
        clear()
        userin.print_blue('||||||||||||||||||| LIST ROUTERS |||||||||||||||')
        routers = self.dev_con.index_router()
        i = 0
        for n in routers:
            print('\n'+str(i)+' '+str(n))
            i = i+1
        input('\nPress any key to continue')
