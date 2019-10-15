
from device import Device
from load_devices import load_devices
from load_hostnames import load_hostnames
from app import app
from network_capture import start_capture
import threading

interface_id = 'wlp4s0'

#Thread for Flask web interface
def interface_thread(n, name):
	app.run(host='0.0.0.0')

t = threading.Thread(target = interface_thread, name = 'site_thread', args=(5,'site_thread'))



devices = load_devices()

device_addresses = []
for device in devices:
	device_addresses.append(device)

hostname_address_dict = {}
alternate_hostnames_dict = load_hostnames()


def get_devices():
	return devices


t.start()
start_capture(interface_id,devices,device_addresses,**alternate_hostnames_dict)
