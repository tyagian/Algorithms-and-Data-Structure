"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.
Example 1: Input: s = "anagram", t = "nagaram"   Output: true
Example 2: Input: s = "rat", t = "car"           Output: false
"""
# using sort func. Time: log(n) since sort use merge sort
def valid_anagram(string, t):
    if sorted(list(string)) ==  sorted(list(t)): 
        return True
    return False


# without using sort func. Hashmap. Time: O(n)
# Dic comparison doesn't check order of keys
def isAnagram(s, t):
        dic_s = dict()
        dic_t = dict()
        
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in dic_s:
                    dic_s[s[i]] += 1
                else:
                    dic_s[s[i]] = 1  
                    
                if t[i] in dic_t:
                    dic_t[t[i]] += 1
                else:
                    dic_t[t[i]] = 1
            #print (dic_s)
            #print (dic_t)       
            if dic_s == dic_t:
                return True
            else:
                return False 

# Generate hashmap using collection counter
from collections import Counter
def check_anagram(s,t):
    if len(s) == len(t):
        if Counter(s) == Counter(t):
           return True
    return False

string = "anagram"
t = "nagaram"
print (f"Valid_anagram check for input using sort func, {string} and {t} is {valid_anagram(string,t)}")
print (f"Valid_anagram check for input using dict, {string} and {t} is {isAnagram(string,t)}")
print (f"Valid_anagram check for input using Collections Counter, {string} and {t} is {isAnagram(string,t)}")
