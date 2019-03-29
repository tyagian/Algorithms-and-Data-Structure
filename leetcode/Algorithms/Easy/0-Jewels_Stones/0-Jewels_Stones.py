# J - jewels, S - stones
# Each char in S is also type of stone you have
# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

## You want to know how many of the stones you have are also jewels.

"""
Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0
"""
# case 1:
print "case 1:"
j = "aA"
s = "aAAbbbb"
count = 0 
for stone in s:
    if stone in j:
        count = count + 1
print count

#case 2:
print "\ncase 2:"
def countJewels(s, j):
    return sum(x in j for x in s)
 
print countJewels("aAAbbbb", "aA")
print countJewels("ZZ", "z")
