import pyshark
capture = pyshark.LiveCapture(interface='br0')

print('STARTING PACKET READ:')
for packet in capture.sniff_continuously():
	if("HTTP" in str(packet.layers)):
		print('Packet from:',packet['ip'].src)
		# print('Packet from:',packet['ip'].src)
