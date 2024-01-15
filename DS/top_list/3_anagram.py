# https://leetcode.com/problems/valid-anagram/description/
"""
Given two strings s and t, return true if t is an anagram of s, 
and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
"""

# approach: 
# first convert word into list and then sort them, if both list are same
# then it's anagram otherwise not. 

# time complexity is O(n log n)
# space complexity is O(n)

# def anagram(s,t):
#     sa = sorted(list(s))
#     ta = sorted(list(t))
#     if sa == ta:
#         return True 
#     return False
# s = "anagram"
# t = "nagaram"
# print (anagram(s,t))
class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = {}
        for char in s:
            s_counter[char] = s_counter.get(char, 0) + 1
        for char in t:
            if char not in s_counter or s_counter[char] == 0:
                return False
            print (s_counter)
            s_counter[char] -= 1
        return True
s = "anagram"
t = "nagaram"
anagram_checker = Solution()
print (anagram_checker.isAnagram(s,t))