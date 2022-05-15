""" Parse apache log file and find out IP address. 
1. We need to count the number of times IP address repeat, which means after parsing if
192.168.0.1
192.168.0.1
We need an output like 192.168.0.1,3
2. We need to save the output of the program in csv file
3. We need to make our program user-friendly which means program should give user some friendly
help output and then give them access to supply the different filename, to solve this I am going
to user argparser module
regex: 
 grep -Po "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" apache_logs.log | sort | uniq -c                                                  
      3 10.10.220.3                                                                                                                                    
      1 127.0.0.1                                                                                                                                      
      1 192.168.2.20   
but this will also filter incorrect ip-address like 9999.999.999.999
so, better regex is 
grep -P -o '(25[0-5]|2[0-4][0-9][01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
"""
import re, csv
from collections import Counter
import argparse

#logfile="apache_logs.log"
logreg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

my_parser = argparse.ArgumentParser(description="read the log file")
my_parser.add_argument("logfile", 
                    help="please enter the logfile to parse",type=argparse.FileType('r'))
args = my_parser.parse_args()
logfile=args.logfile

with logfile as f:
    fread = f.read()
    #print (log)
    ip_list = re.findall(logreg, fread)
    count = Counter(ip_list)
    #top_2_ips = count.most_common(2)
    #print (count)
    
    with open("ipcount.csv","w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow(["IP_Address","Count"])
        for k,v in count.items():
            fwritercsv.writerow([k,v])
    