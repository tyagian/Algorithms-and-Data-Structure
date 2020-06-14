#from json import load as json_load
import json
import csv
with open("sample_input.json") as input_file: 
    people = json.load(input_file)
    with open("save_output.csv", 'w') as csvfile:
        #print (person["name"], person["city"])
        fieldnames = ["name", "city","age"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for person in people["people"]:
            if person["age"] >= 25:
                writer.writerow(person)