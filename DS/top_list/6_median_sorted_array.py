#4. Median of Two Sorted Arrays
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1: Input: nums1 = [1,3], nums2 = [2], Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2: Input: nums1 = [1,2], nums2 = [3,4], Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
def median_array(nums1,nums2):
    nums3 = sorted(nums1 + nums2)
    n = len(nums3)
    if n % 2 != 0:
        median = nums3[int(n/2)]
    else:
        b = int(n/2)
        a = b-1
        median = (nums3[int(n/2)-1] + nums3[int(n/2)]) / 2
    return median
nums1 = [1,5]
nums2 = [6,9]
print (median_array(nums1,nums2))