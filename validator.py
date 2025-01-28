import re

def validate_ip(ip_address):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip_address):
        octets = ip_address.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False

def validate_subnet_mask(subnet_mask):
    valid_masks = [
        "255.0.0.0", "255.128.0.0", "255.192.0.0", "255.224.0.0", "255.240.0.0",
        "255.248.0.0", "255.252.0.0", "255.254.0.0", "255.255.0.0", "255.255.128.0",
        "255.255.192.0", "255.255.224.0", "255.255.240.0", "255.255.248.0",
        "255.255.252.0", "255.255.254.0", "255.255.255.0", "255.255.255.128",
        "255.255.255.192", "255.255.255.224", "255.255.255.240", "255.255.255.248",
        "255.255.255.252", "255.255.255.254"
    ]
    return subnet_mask in valid_masks

