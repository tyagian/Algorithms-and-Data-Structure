"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        #print ("res:",res)
        left_prod, right_prod = 1, 1
        for i in range(len(nums)):
            res[i] *= left_prod
            #print ("res[i]:",res[i])
            res[~i] *= right_prod
            #print ("res[~i]:",res[~i])
            left_prod *= nums[i]
            #print ("left_prod: ", left_prod)
            right_prod *= nums[~i]
            print ("right_prod: ", right_prod)
            print ("\n\n")
        return res
if __name__=="__main__":
    nums = [5,2,6,4,1,2,3]
    print (Solution().productExceptSelf(nums))