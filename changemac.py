#! /usr/bin/python3
import os
import scapy.interfaces as sci
from scapy.config import conf
from scapy.arch import get_if_hwaddr

ifaces = sci.get_if_list()
for iface in sci.get_if_list():
    print(iface + ': '+get_if_hwaddr(iface))

    

    
    

# if os.name != 'posix': #NOTE Linux
#     print('Your OS is not linux')
#     exit(0)

# if os.getuid() != 0:
#     print('sudo permitted! ')
#     exit(0)

# os.system('ifconfig')
