import csv
"""
with open("sample_input.csv") as input_file:
    people = csv.reader(input_file)
    for row in people:
        if row[1] > str(30):
            print (row[0] + row[2])
"""
with open("sample_input.csv") as input_file:
    people = csv.reader(input_file)   
    headers = next(people)
    for row in people:
        #print(row)
        person = (dict(zip(headers, row)))
        #print(people)
        if person["age"] >= str(30):
            print("Name: {name}, City: {city}".format(name=person["name"], city=person["city"]))
 
