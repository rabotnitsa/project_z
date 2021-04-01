"""
Program: Puts Wireless adapter into monitor mode
Steps: 
    ifconfig
    ifconfig wlan0 down
    iwconfig wlan0 mode monitor
    ifconfig wlan0 up
Features: Allows user to decide the interface    
"""
import subprocess
import optparse
import re

#defines user arguments
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Select wireless device")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("\n \n [-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("\n \n [-] Please specify a new mac address, use --help for more info.")
    return options

#defining the interface that will be changed from "managed" to "monitor" mode
def set_wireless(interface):
    print("\n \n [+] Puting " + interface + " into monitor mode ")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["iwconfig", interface, "mode", "monitor"])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()

print("Done")
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
