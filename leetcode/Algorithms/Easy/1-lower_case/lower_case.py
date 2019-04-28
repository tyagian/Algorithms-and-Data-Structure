#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""
Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""
def tolower(input_str):
  output = ""
  for char in input_str:
    if char >= "A" and char <= "Z":
      output = output + chr(ord(char) + 32)
    else:
        output = output + char
  return output

print tolower("Hello")
