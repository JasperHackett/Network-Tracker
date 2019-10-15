import pyshark

primary_hostname = 'none'

def start_capture(interface_id,devices,device_addresses,**alternate_hostnames):
	capture = pyshark.LiveCapture(interface=interface_id)

	print('STARTING PACKET READ:')
	for packet in capture.sniff_continuously():
		if 'HTTP' in packet or 'SSL' in packet:
			for ip in device_addresses:
				if packet['ip'].src == ip:
					if 'SSL' in packet:
						if 'handshake_extensions_server_name' in packet.ssl.field_names:
							# print('SNI of visited site :',packet.ssl.handshake_extensions_server_name)
							# primary_hostname = 'none'
							print('SNI of visited site :',packet.ssl.handshake_extensions_server_name)
							if check_address(packet.ssl.handshake_extensions_server_name,**alternate_hostnames) is True:
								for device in devices:
									if device.ip_address == ip:
										device.add_visited(primary_hostname)




# Checks if a Subject Name Indicator field in the packet matches an entry in the dictionary for a site. 
# For example: 'assets.nflxext.com' will match netflix.com
def check_address(dst_address,**alternate_hostnames):

	# found = False
	global primary_hostname
	i = 0
	for primary, alternate in alternate_hostnames.items():
		for name in alternate:
			# print(name)
			if dst_address == name:
				primary_hostname = primary
				# print('PRIMARY HOSTNAME: ', primary_hostname)
				return True
				print("Site visited:",primary)
		++i

	return False
