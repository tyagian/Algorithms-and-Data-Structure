""" Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets. Example: Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is: [  [-1, 0, 1],  [-1, -1, 2] ]
https://leetcode.com/problems/3sum/discuss/624953/Python3-Solution  """

def threeSum3(nums):
    import collections
    res = []
    c = collections.Counter(nums) # count the value appear time
    #Counter({-1: 2, 0: 1, 1: 1, 2: 1, -4: 1})
    import itertools
    for u, v in itertools.combinations_with_replacement(c, 2):
        #print(u,v)
        w = -u-v
        flag = False
        if w not in c:
            continue
        elif u == v == w:
            flag = c[u] > 2 #at least 3 duplicate value
        elif u == v:
            flag = c[u] > 1 #at least 2 duplicate value
        elif u < w and v < w: # no duplicate value
            flag = True

        if flag:
            res.append([u, v, w])
    return res
print (threeSum3([-1, 0, 1, 2, -1, -4]))