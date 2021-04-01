#!/bin/python3
"""
Program: Mac Address Changer
-Need to be able to execute linux terminal commands
-to do this python module called 'subprocess' --> execute system commands
-commands depend on the os which executesd the script
"""

import subprocess
import optparse
import re

def get_arguments():
    # adding arguments for users
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n \n [-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("\n \n [-] Please specify a new mac address, use --help for more info.")
    return options

def change_mac(interface, new_mac):
    print("\n \n [+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    print(ifconfig_result)
    #mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    #if mac_address_search_result:
    #   return mac_address_search_result.group(0)
    #else:
    #    print("[-] Could not read MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)

print("Current MAC = ", str(current_mac))
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)




#def show_mac(interface):
    #if"-s" == True:
    #    show_interface = subprocess.call(["ifconfig", interface])
    #   print(show_interface)
#    else:
#        print("nada")

#initialize variable#
#interface = options.interface
#new_mac = options.new_mac


#show_mac(options.interface)

#print in terminal
#print("[+] Changing MAC address for " + interface +" to "+ new_mac)

######
#CODE#
######
#executes shells commands in terminal
#subprocess.call(["ls", "-l"])
#subprocess.call("ls -l", shell=True)
#if struggling to change, connect to argentina servver
#subprocess.call("sudo ifconfig wlp0s20f3 down", shell=True)
#subprocess.call(["ifconfig", interface, "down"])
#subprocess.call("sudo ifconfig wlp0s20f3 hw ether 11:22:33:44:55:66", shell=True)
#for some reason starting with 00 or 11 was not working, changed confirgureation below and works
#subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#subprocess.call("sudo ifconfig wlp0s20f3 up", shell=True)
#subprocess.call("ifconfig enp4s0 up", shell=True)
#subprocess.call(["ifconfig", interface, "up"])

######
#Data#
######
#logical name: wlp0s20f3
#serial: 40:ec:99:21:74:2e
#logical name: enp4s0 (internet ran fine without)
#serial: 00:2b: 67:1e: 21:ab