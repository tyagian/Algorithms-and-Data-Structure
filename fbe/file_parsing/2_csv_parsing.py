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
"""
#headers_1 = []
set_1 = []
LEG_LENGTH = []
with open("dataset_1.csv",'r') as file_1:
    read_file1 = csv.reader(file_1)
    headers_1 = next(read_file1)
    for row in read_file1:
        set_1.append(row)
        LEG_LENGTH.append(row[1])
#headers_2 = []
set_2 = []
STRIDE_LENGTH = []
with open("dataset_1.csv",'r') as file_1:
    read_file2 = csv.reader(file_1)
    headers_2 = next(read_file2)
    for row in read_file2:
        set_2.append(row)
        STRIDE_LENGTH.append(row[1])
"""

"""
    read_file1 = csv.reader(file_1)
    for f2 in read_file2:
        #print (f2)
        if f2[2] == "bipedal":
            print (f2)
"""    
"""
    for f2,f1 in zip(file_1, file_2):
        #print(f2)
        #print(f1)
        if f2[2] == "bipedal" and f1[0] == f2[0]:
            print("\t".join(f2, f1))
"""
