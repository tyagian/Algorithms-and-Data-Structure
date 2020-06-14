"""
"name","age","city"
"John",30,"Chicago"
"Beth",21,"New York"
"Lucy",25,"Los Angeles"
"Amey",28,"DC"
"Anuj",28,"Philly"
Print name, city and age of people with age > 25
"""
import csv
with open("sample_input.csv",'r') as i_file:
   reader = csv.DictReader(i_file)
   headers = reader.fieldnames
   print ("headers:",headers)
   for info in reader:
       name, age, city = info.get("name"), info.get("age"), info.get("city")
       if not name or not age or not city:
           continue 
       if int(info["age"]) > 25:
            with open("save_output.csv", 'w') as csvfile:
                fieldnames = ["name", "city","age"]
                print (info["name"], info["city"])
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'name': info["name"], 'city': info["city"], 'age': info["age"]})


print ("info:",info)          
# Time: O(n), Space: min(n)
