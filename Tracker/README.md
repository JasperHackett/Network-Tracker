#Installation#

Required Python packages:
pyshark
flask

Unix packages:
bridge-utils

#Setup#

Two ethernet interfaces are required to setup the tracker for multiple devices. A list of your interface names can be found by typing ifconfig into terminal

Bridging interfaces:
Open bridge_setup.sh and edit the 2nd line to include the name of the two interfaces to bridge after 'brctl addif br0 '. Edit the 4th line to include the first interface and the 5th to include the second.

Then run bridge_setup.sh as root


Single interface:
For tracking a single device, open terminal and type ifconfig to find the name of the interface you wish to track. This can then be set in the Network Configuration section of the web interface

This mode will only track a single device



#Running Application#

In order to start the network tracker run main.py as root

The web interface will be hosted locally on port 5000 (localhost:5000)

Navigate to Network Configuration and set your interface name. If you are running in bridge mode set up with the bridge_setup.sh file, the interface name should be 'br0'.
Alternatively set the interface name to the ID provided in ifconfig (via Terminal) of the NIC you want to track.

Note: After changing the Network Interface Card name the application will need to be restarted for the changes to take effect.

Navigate to the devices page to add devices that you want to track. The device name uses a friendly name and does not need to be the hostname of the device.


