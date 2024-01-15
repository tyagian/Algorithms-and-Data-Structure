# Two Sum: https://leetcode.com/problems/two-sum/?envType=featured-list&envId=top-interview-questions
""" Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
"""
def twosum(l, target):
    result = []
    for i in l:
        if (target - i) in l and i not in result:
                if l.index(target - i) != l.index(i):
                    result.append(l.index(i))
    return result
l = [3,2,4]
target = 6
print (twosum(l,target))