import subprocess
# Write a Python program to get system command output.

if __name__ == "__main__":
    data = subprocess.check_output("dir", shell=True)
    print(data)