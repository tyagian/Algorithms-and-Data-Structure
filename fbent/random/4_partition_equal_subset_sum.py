"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Note: Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1: Input: [1, 5, 11, 5], Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2: Input: [1, 2, 3, 5], Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
"""
# Case1: Using lambda
#https://leetcode.com/problems/partition-equal-subset-sum/discuss/609458/Python3-2-lines-32ms-bitset-solution-Partition-Equal-Subset-Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, r = divmod(sum(nums), 2)
        return r == 0 and (reduce(lambda x, y: x << y | x, [1] + nums) >> target) & 1

# Case2:
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90610/Python-Backtracking-with-Memoization-Solution

class Solution:
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: return d[target] 
        if target == 0: d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]
          
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, len(nums), {})
# Case:3
# DP and DFS
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/276278/Python-DP-and-(DFS%2BMemo)
"""
class Solution(object):
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: return d[target] 
        if target == 0: d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]
    
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, len(nums), {})

test = Solution().canPartition([1,5,11,5])
print (test)