brctl addbr br0
brctl addif br0 enx00e04c6802f0 enp0s31f6
ifdown br0
ifup enx00e04c6802f0 
ifup enp0s31f6
ifup br0



