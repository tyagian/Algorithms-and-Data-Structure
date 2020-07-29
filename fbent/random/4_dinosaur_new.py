import csv, math
from operator import itemgetter

g = 9.8
dino = {}
speed_dict = {}
class Solution:
    def dino(file_1, file_2):
        with open("dataset_2.csv") as file2:
            reader = csv.DictReader(file2)
            for row in reader:
                name, str_len, stance = row.get('NAME'), row.get('STRIDE_LENGTH'), row.get('STANCE')  
                if not name or not str_len or not stance:
                    continue 
                if stance == 'bipedal':
                    dino[name] = str_len
        with open("dataset_1.csv") as file1:
            reader = csv.DictReader(file1)
            for row in reader:
                name, leg_len = row.get('NAME'), row.get('LEG_LENGTH')
                if not name or not leg_len or name not in dino:
                    continue
                str_len = dino[name]
                #speed = ((float(str_len / leg_len)) - 1) * math.sqrt(float(leg_len) * g)
                speed = ((float(str_len) / float(leg_len)) - 1) * math.sqrt(float(leg_len) * g)
                speed_dict[name] = speed
        #print (speed_dict)
        print (*[key for key, value in sorted(speed_dict.items(), key = lambda kv: kv[1], reverse=True)], sep='\n')
        
#print (speed_dict)
#print ("\tNAME: \t\t Speed")
#for key, value in sorted(speed_dict.items(), itemgetter(1), reverse=True):
#    print("%s: %s" %(key, value))

# Time Complexity: O(n) + if - Const + value assign - Const
# O(m) + similarly const
#  min(m,n)
# print line 31 - min(m,n) log(min(m,n))
# O(n) + O(m) + min(m,n) + C
# O(n) + O(m)

## Space: 
# Dino {} - O(n)
# speed_dict = {} - min (m,n)
# Space: O(n)
print (Solution.dino("dataset_1.csv", "dataset_2.csv"))