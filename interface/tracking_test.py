import pyshark
cap = pyshark.LiveCapture(interface=2)
cap.sniff(timeout=10)
print(cap)

import pyshark
cap = pyshark.FileCapture('wlan.pcap',only_summaries=True) 
dir(cap[0])