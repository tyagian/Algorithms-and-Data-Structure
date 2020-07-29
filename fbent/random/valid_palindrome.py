"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
Input: "race a car"
Output: false
"""
class Solution:
    def isPalindrome(s):
        if len(s) == None: return None
        if len(s) == 1: return True
        if len(s) > 1:
            s = list(filter(str.isalnum, s))
            for i in range (0,len(s)//2):
                if s[i].casefold() != s[-i-1].casefold(): # remove case usecase
                    return False
        return True


print (Solution.isPalindrome("A man, a plan, a canal: Panama"))












