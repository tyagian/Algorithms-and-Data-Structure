#https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-2/

# approach 1:
try:
    with open("abc.txt") as f:
        print (f.read())

except Exception as e:
    print (e)

#approach 2: using os
import os
filename="/etc/hosts"
if os.path.exists(filename) and os.path.isfile(filename):
    print("File exist")
else:
    print("File doesn't exist")

#approach 3:
path = pathlib.Path("/etc/hosts")
path.exists()
path.is_file()
