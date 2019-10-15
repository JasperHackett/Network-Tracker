
from device import Device
from load_devices import load_devices
from load_hostnames import load_hostnames
from app import app
from network_capture import start_capture
import threading

interface_id = 'wlp4s0'

#Thread for Flask web interface
def interface_thread(devices, name):
	# print('THREAD PRINT',devices)
	app.run(host='0.0.0.0')


devices = load_devices()

t = threading.Thread(target = interface_thread, name = 'site_thread', args=(devices,'site_thread'))





device_addresses = []
for device in devices.values():
	# print(device.ip_address)
	device_addresses.append(device.ip_address)

# print(device_addresses)
hostname_address_dict = {}
# print("TIDY HOSTNAME:")

alternate_hostnames_dict = load_hostnames()
# print(alternate_hostnames_dict)


# for hostname in alternate_hostnames_dict.values():
	# print(hostname)


def get_devices():
	return devices

t.start()
start_capture(interface_id,devices,device_addresses,**alternate_hostnames_dict)

