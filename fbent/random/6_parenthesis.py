"""
20. Valid Parentheses. Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(s):
        stack=[]
        for i in range(len(s)):
            #print ("(s[i]: ",s[i])
            #print ("stack: ",stack)
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
                #print("stack appended:",stack)
            else:
                if stack:
                    if (s[i]==')' and stack[-1]!='(') or (s[i]=='}' and stack[-1]!='{') or (s[i]==']' and stack[-1]!='['):
                        #print ("stack match")
                        return False
                    else:
                        #print ("pop")
                        stack.pop()
                else:
                    return False
        #print(stack)
        if len(stack)!=0:
            return False
        else:
            return True

s = "()[]{}"
print (Solution.isValid(s))
