import socket
# Write a Python program to get the name of the host on which the routine is running.

if __name__ == "__main__":
    print(socket.gethostname())