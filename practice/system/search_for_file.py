#https://www.101daysofdevops.com/courses/101-days-of-devops/lessons/day-3-2/
import os
for dirpath, dirname, filename in os.walk("/etc"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == "hosts":
            print(comp_path)

# case2:
import argparse
my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
my_parser.add_argument("pathname",help='Please enter the directory path ')
my_parser.add_argument("filesearch",help='Please enter the filename to search')
args = my_parser.parse_args()
for dirpath, dirname, filename in os.walk(args.pathname):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == args.filesearch:
            print(comp_path)
"""
python3 find_files.py /etc hosts
/etc/hosts
"""
