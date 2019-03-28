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
j = "aA"
s = "aAAbbbb"

S_list = s.split()
J_list = j.split()
count = 0 
print S_list
print J_list

for stones in S_list:
    for jeweles in J_list:
        if stones == jeweles:
            count = count + 1
print count

def countJewels(s, j):
    return sum(x in j for x in s)
 
print countJewels("aAAbbbb", "aA")
print countJewels("ZZ", "z")
