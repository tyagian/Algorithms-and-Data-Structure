# Validate if a given string is a valid email address:
import re

def is_valid_email(email):
  return bool(re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email)) 

print(is_valid_email("test@example.com")) # True
print(is_valid_email("invalid@@email.com")) # False