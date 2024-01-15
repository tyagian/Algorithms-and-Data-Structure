# Extract dates from a string:
import re 

def extract_dates(text):
  return re.findall(r'\d{1,2}\/\d{1,2}\/\d{2,4}', text)
  
text = "Dates such as 4/5/2021, 7/8/2020 are in this text"
print(extract_dates(text)) 
# ['4/5/2021', '7/8/2020']
