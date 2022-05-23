"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.
Example 1: Input: nums = [1,2,3,1]              Output: true
Example 2: Input: nums = [1,2,3,4]              Output: false
Example 3: Input: nums = [1,1,1,3,3,4,3,2,4,2]  Output: true
"""
# Simple approach
def dup_test(nums):
    d = {}
    for i in nums:
        if i in d:
            return True
        d[i] = 1
    return False

# using set func
def dup_test1(nums):
    if len(set(nums)) == len(nums):
        return False
    return True
#The first approach takes more time but less space than second approach.
nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

print (f"First approach: \n {dup_test(nums1)} \n {dup_test(nums2)} \n {dup_test(nums3)}")
print (f"Second approach: \n {dup_test1(nums1)} \n {dup_test1(nums2)} \n {dup_test1(nums3)}")

