from netaddr import IPAddress, IPNetwork

def load_config(config):
  address = IPAddress(config["address"])
  network = IPNetwork(config["network"])
