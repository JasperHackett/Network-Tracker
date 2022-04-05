
#Object for a device on the network
class Device():
    ip_address = '0.0.0.0'
    visited_sites = []
    active_site = "None"
    mac_address = '00:00:00:00:00:00'

    def __init__(self, friendly_name,ip_address):

        self.friendly_name = friendly_name
        # self.friendly_name = host_name
        # self.friendly_name = mac_address
        self.ip_address = ip_address.rstrip()

    def add_visited(self,hostname):
        # print(self.friendly_name ,' visited a site')
        if(self.active_site != hostname):
            self.active_site = hostname

            out_str = self.friendly_name + ' is now visiting the site: ' + hostname + '\n'
            f = open("activity_log","a+")
            f.write(out_str)
            f.close() 
            # print(self.friendly_name, ' is now visiting the site: ', hostname)
