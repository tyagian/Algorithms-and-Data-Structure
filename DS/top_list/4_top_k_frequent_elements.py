# https://leetcode.com/problems/top-k-frequent-elements/
"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
class Solution:
    def top_k_frequent(self,nums, k):
        count_chars = {}
        for num in nums:
            if num in count_chars and count_chars[num] >= 1:
                count_chars[num] = count_chars.get(num,0) + 1
            elif num not in count_chars:
                count_chars[num] = 1
        result = []
        for key, value in count_chars.items():
            if count_chars[key] >= k:
                result.append(key)
                
        return result

top_elements = Solution()
nums = [1,1,1,2,2,3]
k = 2
print (top_elements.top_k_frequent(nums, k))