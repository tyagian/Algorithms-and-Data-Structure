"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
## Case-1
def twoSum(nums, target):
        i = 0 
        j = 1 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    ans = [ i, j ]
                    j += 1
            i += 1
        return ans

nums = [2,7,11,15]
target = 18
print (twoSum(nums, target)) 

## Case -2 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            if num in sums: # Number is in remainder, access hashmap to find the index of the second number
                return [sums[num], i]
            else:
                sums[target - num] = i
"""