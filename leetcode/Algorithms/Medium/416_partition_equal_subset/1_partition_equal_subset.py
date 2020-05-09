"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr = nums
        arr.sort()
        if sum(arr)%2 != 0: return False

        expected = sum(arr)/2
        i = curr = 0

        while curr < expected:
            curr += arr[i]
            i += 1
        return True if curr == expected else False