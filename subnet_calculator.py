import ipaddress

def calculate_subnet_info(ip_address, subnet_mask):
    # Combine IP and subnet mask into a network object
    network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)

    # Extract subnet information
    return {
        "Network Address": str(network.network_address),
        "Broadcast Address": str(network.broadcast_address),
        "Subnet Mask": str(network.netmask),
        "Number of Hosts": network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses,
        "First Host": str(network.network_address + 1),
        "Last Host": str(network.broadcast_address - 1),
    }
