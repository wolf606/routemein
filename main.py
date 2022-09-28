import imp
import os
from Library.UserInputLib import userInputLib as userin
from Library.Views.NetworkView import NetworkView
from Library.Views.DeviceView import DeviceView

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

net_v = NetworkView()
dev_v = DeviceView()

def menu() -> None:
    menu_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** Cisco Router Command Generator **********\n\n'
    +'  1.'+' Networks\n'
    +'  2.'+' Devices\n'
    +'  3.'+' Add Devices to Networks\n'
    +'  4.'+' Generate CLI commands\n'                
    +'  5.'+' Exit\n'
    +'\nOption: ')

def menu_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            menu_networks()
        elif answer == '2':
            menu_devices()
        elif answer == '3':
            menu_add_devs_to_nets()
        elif answer == '4':
            pass
        elif answer == '5':
            clear()
            break
        else:
            print('\nNot a valid option')

def menu_networks() -> None:
    menu_networks_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** NETWORKS **********\n\n'
    +'  1.'+' WANS\n'
    +'  2.'+' LANS\n'
    +'  3.'+' VLANS\n'                   
    +'  4.'+' Back to main menu\n'
    +'\nOption: ')

def menu_networks_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            menu_wans()
        elif answer == '2':
            menu_lans()
        elif answer == '3':
            pass
        elif answer == '4':
            break
        else:
            print('\nNot a valid option')

def menu_lans() -> None:
    menu_lans_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** LANS **********\n\n'
    +'  1.'+' Add\n'
    +'  2.'+' List\n'                  
    +'  3.'+' Back to main menu\n'
    +'\nOption: ')

def menu_lans_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            net_v.add_lans()
        elif answer == '2':
            net_v.list_lans()
        elif answer == '3':
            break
        else:
            print('\nNot a valid option')

def menu_wans() -> None:
    menu_wans_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** WANS **********\n\n'
    +'  1.'+' Add\n'
    +'  2.'+' List\n'                  
    +'  3.'+' Back to main menu\n'
    +'\nOption: ')

def menu_wans_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            net_v.add_wans()
        elif answer == '2':
            net_v.list_wans()
        elif answer == '3':
            break
        else:
            print('\nNot a valid option')
  
def menu_devices() -> None:
    menu_devices_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** DEVICES **********\n\n'
    +'  1.'+' Routers\n'
    +'  2.'+' PCs\n'
    +'  3.'+' Switches\n'                   
    +'  4.'+' Back to main menu\n'
    +'\nOption: ')

def menu_devices_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            menu_routers()
        elif answer == '2':
            pass
        elif answer == '3':
            pass
        elif answer == '4':
            break
        else:
            print('\nNot a valid option')

def menu_routers() -> None:
    menu_routers_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** Routers **********\n\n'
    +'  1.'+' Add\n'
    +'  2.'+' List\n'                  
    +'  3.'+' Back to main menu\n'
    +'\nOption: ')

def menu_routers_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            if not net_v.is_wans_empty(): dev_v.add_routers()
            else: userin.print_err('NO WANS HAVE BEEN CREATED YET'); input('\nPress any key to continue')
        elif answer == '2':
            dev_v.list_routers()
        elif answer == '3':
            break
        else:
            print('\nNot a valid option')

def menu_add_devs_to_nets() -> None:
    menu_add_devs_to_nets_calls(
    '\n\n||||||||||||||||||||||||||||||||||||||'
    +'\n********** Add devices to networks **********\n\n'
    +'  1.'+' Add routers to WANs\n'
    +'  2.'+' Add PCs to LANs\n'              
    +'  3.'+' Back\n'
    +'\nOption: ')

def menu_add_devs_to_nets_calls(text_input: str) -> None:
    while True:
        clear()
        answer = input(text_input)
        if answer == '1':
            net_v.add_routers_to_wan(dev_v.dev_con)
        elif answer == '2':
            menu_lans()
        elif answer == '3':
            break
        else:
            print('\nNot a valid option')

if __name__ == "__main__":
    menu()