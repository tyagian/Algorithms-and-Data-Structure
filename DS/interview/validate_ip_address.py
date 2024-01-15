# Validate an IP Address
import re

def validate_ip_address(ip):
    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    if ipv4_pattern.match(ip):
        return "IPv4"
    elif ipv6_pattern.match(ip):
        return "IPv6"
    else:
        return "Invalid"

# Example
print(validate_ip_address("192.168.1.1"))  # Output: IPv4
print(validate_ip_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: IPv6
