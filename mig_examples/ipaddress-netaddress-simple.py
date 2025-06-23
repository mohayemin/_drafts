from ipaddress import ip_address, ip_network

def load_config(config):
    address = ip_address(config["address"])
    network = ip_network(config["network"], strict=False)
