""" You will be supplied with two data files in CSV format. The  first file contains statistics about various dinosaurs. The second file contains additional data. 
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) Where g = 9.8 m/s^2 (gravitational constant) 
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest. 
Do not print any other information. 
$ cat dataset1.csv                          |   $ cat dataset2.csv 
NAME,LEG_LENGTH,DIET                        |   NAME,STRIDE_LENGTH,STANCE
Hadrosaurus,1.2,herbivore                   |   Euoplocephalus,1.87,quadrupedal
Struthiomimus,0.92,omnivore                 |   Stegosaurus,1.90,quadrupedal
Velociraptor,1.0,carnivore                  |   Tyrannosaurus Rex,5.76,bipedal
Triceratops,0.87,herbivore                  |   Hadrosaurus,1.4,bipedal
Euoplocephalus,1.6,herbivore                |   Deinonychus,1.21,bipedal
Stegosaurus,1.40,herbivore                  |   Struthiomimus,1.34,bipedal
Tyrannosaurus Rex,2.5,carnivore             |   Velociraptor,2.72,bipedal """
## STRIDE_LENGTH
## LEG_LENGTH
import csv, math
set_2 = []
STRIDE_LENGTH = []
g = 9.8
table3 = {}
table4 = {}
with open("dataset_2.csv") as file2:
    table2 = csv.DictReader(file2)
    for rows2 in table2:
        if rows['STANCE'] == 'bipedal':
            STRIDE_LENGTH = row2['STRIDE_LENGTH']
            table3[(rows2['NAME'])] = rows2['STRIDE_LENGTH']
with open("dataset_1.csv") as file1:
    table1 = csv.DictReader(file1)
    for rows1 in table1:
       if rows1['NAME'] in table3:
           STRIDE_LENGTH = table3[key]
           speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
           table4[key] = float(speed)
print ("\tNAME : \t\t Speed")
for key, value in sorted(table4.items(), key = lambda kv: kv[1], reverse=True):
    print("%s: %s" %(key, value))

