
from device import Device
from load_devices import load_devices
from load_hostnames import load_hostnames
from app import app
from network_capture import start_capture
import threading

# Loads the name of the network interface card to be tracked from the nic_id file
interface_id = 'br0'
with open('nic_id') as f:
	for line in f:
		interface_id = line

#Thread for Flask web interface
def interface_thread(devices, name):
	# print('THREAD PRINT',devices)
	app.run(host='0.0.0.0')

#Load list of devices
devices = load_devices()

t = threading.Thread(target = interface_thread, name = 'site_thread', args=(devices,'site_thread'))

device_addresses = []
for device in devices.values():
	# print(device.ip_address)
	device_addresses.append(device.ip_address)

#Loads tracked hostnames
hostname_address_dict = {}
alternate_hostnames_dict = load_hostnames()


def get_devices():
	return devices

#Starts flask thread for interface
t.start()
#Starts network packet capture
start_capture(interface_id,devices,device_addresses,**alternate_hostnames_dict)

