# Find all numbers in a string:
import re

def find_numbers(text):
  return re.findall(r'\d+', text)

print(find_numbers("This text has 123 and 456 numbers")) 
# ['123', '456']