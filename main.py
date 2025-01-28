from input_handler import get_ip_and_mask
from validator import validate_ip, validate_subnet_mask
from subnet_calculator import calculate_subnet_info

def main():
    print("Welcome to the Subnet Finder!")

    # Get user input
    ip_address, subnet_mask = get_ip_and_mask()

    # Validate IP address and subnet mask
    if not validate_ip(ip_address):
        print("Invalid IP address format.")
        return

    if not validate_subnet_mask(subnet_mask):
        print("Invalid subnet mask.")
        return

    # Calculate subnet details
    subnet_info = calculate_subnet_info(ip_address, subnet_mask)
    print("\nSubnet Details:")
    for key, value in subnet_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
