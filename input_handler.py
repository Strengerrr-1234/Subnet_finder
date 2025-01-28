def get_ip_and_mask():
    ip_address = input("Enter the IP address (e.g., 192.168.1.1): ").strip()
    subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ").strip()
    return ip_address, subnet_mask
