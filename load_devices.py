#Loads the IP address/device names to be tracked
from device import Device

def load_devices():
	d = {}

	with open("device_list") as f:
		for line in f:
			(key,val) = line.split(':')
			d[key] = Device(key,val)
	return d

