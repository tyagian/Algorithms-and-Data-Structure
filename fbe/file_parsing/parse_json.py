#from json import load as json_load
import json

with open("sample_input.json") as input_file:
    people = json.load(input_file)
    for person in people["people"]:
        if person["age"] >= 30:
            print("Name: {name}, City: {city}".format(name=person["name"], city=person["city"]))
