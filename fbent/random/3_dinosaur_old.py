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
g = 9.8
#table3 = {}
#table4 = {}
dino = {}
speed_dict = {}
with open("dataset_2.csv") as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        if row['STANCE'] == "bipedal":
            #STRIDE_LENGTH = row['STRIDE_LENGTH']
            dino[(row['NAME'])] = row['STRIDE_LENGTH']
    #print (dino)
with open("dataset_1.csv") as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        if row['NAME'] in dino:
            LEG_LENGTH = row['LEG_LENGTH']
            STRIDE_LENGTH = table3[rows2['NAME']]
            speed = ((float(STRIDE_LENGTH) / float(LEG_LENGTH)) - 1) * math.sqrt(float(LEG_LENGTH) * g)
            speed_dict[row['NAME']] = float(speed)
    #print (speed_dict)
print ("\tNAME : \t\t Speed")
for key, value in sorted(speed_dict.items(), key = lambda kv: kv[1], reverse=True):
    print("%s: %s" %(key, value))


# Time Complexity: O(n) + if - Const + value assign - Const
# O(m) + similarly const
#  min(m,n)
# O(n) + O(m) + min(m,n) + C
# O(n) + O(m)