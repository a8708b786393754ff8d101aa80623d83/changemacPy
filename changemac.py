#! /usr/bin/python3
import os 

if os.name != 'posix': #NOTE Linux
    print('Your OS is not linux')
    exit(0)

if os.getuid() != 0: 
    print('sudo permitted! ')
    exit(0)