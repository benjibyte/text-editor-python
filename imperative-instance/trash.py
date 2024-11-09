import platform
get_os = platform.system()

if get_os == "Windows":
    print("I am using a Windows PC!")
elif get_os == "macOS":
    print("I was rich!")
else:
    print("I am on linux")
