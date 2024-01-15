#Replace whitespaces between words with a dash:
import re

def dash_separate(text):
  return re.sub(r'\s+', '-', text)
  
print(dash_separate("This text will be dash separated"))
# 'This-text-will-be-dash-separated'