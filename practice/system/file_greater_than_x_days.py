# https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-4/
# A Python script to search files greater than X days old
import os
import datetime

file_age=15
today_date=datetime.datetime.now()

for dir,dirpath,filename in os.walk("/var/log"):
    for file in filename:
        complete_path=os.path.join(dir,file)
        file_creation_time=datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
        time_diff=(today_date-file_creation_time).days
        if time_diff> file_age:
            print(complete_path, time_diff)