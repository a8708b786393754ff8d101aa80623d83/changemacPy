#! /usr/bin/python3.10
import os
import string
import random

from scapy.arch import get_if_list
from scapy.arch import get_if_hwaddr


if os.name != 'posix':  # NOTE Linux
    raise NotImplementedError
    exit(0)
#
if os.getuid() != 0:
    print('Do you have superuser rights?')
    exit(0)

def get_random_mac_address():
    """Generate and return a MAC address in the format of Linux"""

    # get the hexdigits uppercased
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    # 2nd character must be 0, 2, 4, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")


ifaces = get_if_list()
for iface in ifaces:
    print(iface + ': ' + get_if_hwaddr(iface))


choice = input('Enter iface choice: ')

is_in = [True for iface in ifaces if iface == choice]  #  [True] or []

if is_in:  # NOTE non vide
    os.system(f'sudo ifconfig {choice} down')
    os.system(f'sudo ifconfig {choice} hw ether {get_random_mac_address()} ')
    os.system(f'sudo ifconfig {choice} up')