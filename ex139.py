import ipaddress
# Write a Python program to validate an IP address.
def val_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return f"Valid IP"
    except ValueError:
        return f"Not a valid IP"

if __name__ == "__main__":
    ip1 = "192.168.0.1"
    ip2 = "400.1.2.2"
    print(val_ip(ip1))
    print(val_ip(ip2))

