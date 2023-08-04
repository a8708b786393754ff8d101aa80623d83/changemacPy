#! /usr/bin/python3
import os
import scapy.interfaces as sci
from scapy.config import conf
from scapy.arch import get_if_hwaddr

ifaces = sci.get_if_list()
for iface in sci.get_if_list():
    print(iface + ': '+get_if_hwaddr(iface))

    
choice = input('Enter iface choice: ')

is_in = [True for iface in ifaces if iface == choice ] # [True] or []

if is_in:  #NOTE non vide
    os.system(f'sudo ifconfig {choice} down')
    os.system(f'sudo ifconfig {choice} hw ether ')
    os.system(f'sudo ifconfig {choice} up')
    

# if os.name != 'posix': #NOTE Linux
#     print('Your OS is not linux')
#     exit(0)

# if os.getuid() != 0:
#     print('sudo permitted! ')
#     exit(0)

# os.system('ifconfig')
