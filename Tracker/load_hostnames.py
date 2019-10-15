#Loads the hostnames and their alternate names to be tested against the SNI field in network packets

def load_hostnames():
	d = {}

	with open("site_list") as f:
		for line in f:
			(key,host_list) = line.split(':')
			val = host_list.split(',')
			clean_list = []
			for host in val:
				host = host.rstrip()
				# print(host)
				clean_list.append(host)
			d[key] = clean_list
	return d