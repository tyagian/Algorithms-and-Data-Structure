# String Parsing:
# Question: Reverse Words in a String
# Write a function to reverse the order of words in a given string while 
# maintaining the order of characters within each word.
def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Example
print(reverse_words("Hello World"))  # Output: "World Hello"
