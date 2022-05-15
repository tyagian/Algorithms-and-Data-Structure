import platform
import os
# 
"""
platform.system()
platform.architecture()
platform.uname()
platform.release() -> kernel version
platform.python_version()
"""
if platform.system() == "Linux":
    os.system(ls)
if platform.system() == "Windows":
    os.system("dir")
else:
     print("Unsupported operating system")