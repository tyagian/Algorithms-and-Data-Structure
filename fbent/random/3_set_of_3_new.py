""" Check if there is a set of 3 elements in an integer array , that adds upto zero? """
#https://leetcode.com/problems/3sum/discuss/631166/Python-360ms-98-faster
import collections
class Solution:
    def threeSum(nums):
        # Set is much faster than List. I'm stuck with TLE for a while until I used Set instead of List
        ans = set()
        if len(nums) < 3: return ans
        #print (nums.count(0))
        # .count() for number of occurences
        # .add() 
        if nums.count(0) >= 3: ans.add((0,0,0))
        nums_set = set(nums)
        numMax, numMin = max(nums_set), min(nums_set)
        if numMax <= 0 or numMin >= 0: return ans
        # Split into two parts, positive and negative, so don't have to iterate the whole nums. It reduces about 70% time.
        setP = set(num for num in nums_set if (num > 0 )) #and num <= -2 * numMin
        print ("setP",setP)
        setN = set(num for num in nums_set if (num < 0 )) #and num >= -2 * numMax
        print ("setN",setN)
        #dictionary to get occurences in values
        #{0: 1, -1: 1, -2: 1, 3: 1, 2: 1, -3: 1, 5: 1, 1: 1}
        count = collections.Counter(nums)
        print ("count:",count)
        for numP in setP:
            for numN in setN:
                #numD exist in the nums set 
                numD= -numP-numN
                print ("numD:",numP,numN,numD)
                if numD in nums_set:
                    #sort to check later with duplicate pairs
                    val=tuple(sorted([numD,numP,numN]))
                    print ("val:",val)
                    #remove duplicate pairs
                    if val.count(numD)<=count[numD] and val.count(numP)<=count[numP] and val.count(numN)<=count[numN]:
                        ans.add(val)
        return ans
print (Solution.threeSum([0, -1,-2,3, 2, -3,5, 1]))