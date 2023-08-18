import platform
# Write a Python program to get OS name, platform and release information.

def os_info():
    sys = platform.system()
    plat = platform.platform()
    re = platform.release()
    ver = platform.version()
    return sys + "   " + plat + "   " + re + ver

if __name__ == "__main__":
    print(os_info())

