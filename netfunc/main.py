#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + crayons.blue(coffeetime) )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + crayons.blue(mycmds) )
            # we'll learn to write code that sends cmds to device here

# start our main script
def main():
    # work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    # ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file
    with open("network.json", "r") as file_data:
        json_data = json.load(file_data)

    print(crayons.yellow("Welcome to the network device command pusher")) # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(json_data) # call function to push commands to devices

# call our main function
main()

