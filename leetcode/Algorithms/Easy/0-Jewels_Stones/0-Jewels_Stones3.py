"""
Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0
"""

def countJewels(stones, jewels):
    jewelset = set(jewels)
    return sum(1 for stone in stones if stone in jewelset)
 
print(countJewels("aAAbbbb", "aA"))
print(countJewels("ZZ", "z"))