import socket
# Write a Python program to find local IP addresses using Python's stdlib.

def IP_addresses():
    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    return addr

if __name__ == "__main__":
    print(IP_addresses())