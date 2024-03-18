# Python Programme Number 42
# IP Check: A simple programme to determine the ip address of a host
# Version 1.0
# Programmer: Mukul Dharwadkar
# Date: 27 March 2006

import socket       # Import the module socket

print \
      """
            WELCOME TO IP CHECK PROGRAMME!!!
                Programme version 1.0

      This programme will enable you to determine the IP
      address of any host you desire. What it cannot do is
      determine the IP of the web client visitor a website
      and the geographical location of the client.
      Those are enhancements planned for the next versions.
      Some enhancements will also be made on UI front to
      present a graphical interface to the user to enter IP address.
      """

# Define the variable to store the name.
name = raw_input("Enter the name of the host / website: ")

addr = socket.gethostbyaddr(name)       # call the function gethostbyaddr from module socket

print addr[2]           # gethostbyname return a tuple containing three part
                        # The original host name, a blank value and IP address
                        # We are currently interested only in the IP address.
                        # Future revisions will include formatting of the
                        # result.

raw_input("Press enter to exit")
