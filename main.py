import requests
import ipaddress
import argparse
from colorama import Fore, Style, init
import sys

# Initialize colorama
init(autoreset=True)

# Function to get the current public IP address
def get_current_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: Could not fetch IP.{Style.RESET_ALL}")
        return None

# Function to check if the IP is in the given ranges
def is_ip_in_ranges(ip, ranges):
    try:
        ip_obj = ipaddress.ip_address(ip)
        for range_str in ranges:
            network = ipaddress.ip_network(range_str.strip(), strict=False)
            if ip_obj in network:
                return True
        return False
    except ValueError as e:
        print(f"{Fore.RED}Error: Invalid IP or range.{Style.RESET_ALL}")
        return False

# Read the IP ranges from the file
def read_ip_ranges(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{file_path}' not found.{Style.RESET_ALL}")
        return None

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Check if your IP is in the specified ranges.")
    parser.add_argument(
        '-f', '--file',
        default='ip_ranges.txt',
        help="Path to the file containing IP ranges (default: ip_ranges.txt)"
    )
    parser.add_argument(
        '--show-ip',
        action='store_true',
        help="Display the current IP address and status on the same line"
    )
    args = parser.parse_args()

    # Get the current IP address
    current_ip = get_current_ip()
    if not current_ip:
        sys.exit(1)  # Exit with code 1 if IP cannot be determined

    # Read the IP ranges from the file
    ip_ranges = read_ip_ranges(args.file)
    if ip_ranges is None:
        sys.exit(1)  # Exit with code 1 if the file is not found

    # Check if the IP is in the ranges
    is_covered = is_ip_in_ranges(current_ip, ip_ranges)

    # Display the result
    if args.show_ip:
        status = f"{Fore.GREEN}Covered{Style.RESET_ALL}" if is_covered else f"{Fore.RED}Not Covered{Style.RESET_ALL}"
        print(f"Current IP: {Fore.CYAN}{current_ip}{Style.RESET_ALL} - Status: {status}")
    else:
        if is_covered:
            print(f"{Fore.GREEN}Covered{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Not Covered{Style.RESET_ALL}")

    # Exit with appropriate code
    sys.exit(0 if is_covered else 1)

if __name__ == "__main__":
    main()