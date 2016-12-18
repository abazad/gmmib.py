#!/usr/share/python

#// 	     Name: GMMiB <Give Me My internet Back>
#// 	   Author: MibMab
#// Description: This script re-enables services disabled after activating monitor mode on an interface.
#//    Services: NetworkManager, networking, network-manager [Case sensitive]
#// 	   Github: https://github.com/MibMab/GMMIB
#//     License: The MIT License (MIT)

#// Hope you like this workaround for enabling WiFi again!
#// [Note: If you're wondering why the interface variable is named nCard, it's because I called it "Networking Card" before.]

import os

os.system("clear")
print("[GMMiB] ~ Interface? [Input Enabled]")
nCard = raw_input("[GMMiB-Input {Interface}] ^ ")
print("")
print("Press any key to \"reboot\" " + nCard + ". CTRL+C to terminate.")
raw_input("[GMMiB-Input {Continue}] ^ ")
print("[GMMiB] ~ Root Password? [Input Enabled]")
os.system("sudo echo [GMMIB] Root aquired")
os.system("sudo airmon-ng stop " + nCard)
print("[GMMiB] ~ 20%")
os.system("sudo airmon-ng check kill")
print("[GMMiB] ~ 40%")
os.system("sudo service networking start")
print("[GMMiB] ~ 60%")
os.system("sudo service network-manager start")
print("[GMMiB] ~ 80%")
os.system("sudo service NetworkManager start")
print("[GMMiB] ~ 100%")
print("\n\n\n[GMMiB] ~ Done. WiFi should be enabled now!\n\nEnjoy!")
