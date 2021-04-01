#!/bin/python3
"""
Program: Mac Address Changer
Execute linux terminal commands to discover current MAC address and then update it.
"""

import subprocess
import optparse
import re

#adding user arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n \n [-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("\n \n [-] Please specify a new mac address, use --help for more info.")
    return options

#defining the interface that will have an updated MAC address
def change_mac(interface, new_mac):
    print("\n \n [+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#defining current MAC address
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    print(ifconfig_result)

options = get_arguments()
current_mac = get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)

print("Current MAC = ", str(current_mac))
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
