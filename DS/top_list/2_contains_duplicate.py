# https://leetcode.com/problems/contains-duplicate/
"""
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true  
"""

# def containsDuplicate(nums):
#     if len(nums) != len(set(nums)):
#         return True
#     return False
        
# nums = [1,2,3,1]
# print (containsDuplicate(nums))


# def containsDuplicates(nums):
#     seen = {}
#     for num in nums:
#         if num in seen and  seen[num] >= 1:
#                 return True
#         seen[num] = seen.get(num, 0) + 1
#     return False
# nums = [1,2,3,1]
# print (containsDuplicates(nums))

def containsDuplicates(nums):
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
    for val in seen.values():
        if val > 1:
            return True
    return False
nums = [1,2,3,1]
print (containsDuplicates(nums))
