"""
You will be supplied with two data files in CSV format. The  first file contains statistics about various dinosaurs. The second file contains additional data. 
Given the following formula, 
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) Where g = 9.8 m/s^2 (gravitational constant) 
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest. 
Do not print any other information. 

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
"""

import csv
import math
set_2 = []
STRIDE_LENGTH = []
g = 9.8
table3 = {}
table4 = {}
with open("dataset_2.csv", newline='') as file_2:
    table2 = csv.DictReader(file_2)
    for rows2 in table2:
        if rows2['STANCE'] == "bipedal":
            STRIDE_LENGTH = rows2['STRIDE_LENGTH']
            table3[(rows2['NAME'])] = rows2['STRIDE_LENGTH']
    #print (table3)

with open("dataset_1.csv", newline='') as file_1:
    table1 = csv.DictReader(file_1)
    for rows1 in table1:
        for key in table3:
            if str(key) == rows1['NAME']:
                LEG_LENGTH = rows1['LEG_LENGTH']
                STRIDE_LENGTH = table3[key]
                #print (rows1['NAME'], str(key))
                speed = ((float(STRIDE_LENGTH) / float(LEG_LENGTH)) - 1) * math.sqrt(float(LEG_LENGTH) * g)
                table4[key] = float(speed)
print ("\tNAME : \t\t Speed")
for key, value in sorted(table4.items(), key = lambda kv: kv[1], reverse=True):
    print("%s: %s" %(key, value))
