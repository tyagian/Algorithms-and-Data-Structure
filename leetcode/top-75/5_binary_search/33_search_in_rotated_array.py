"""
Search in rotated sorted array
memory: O(log n) since binary search used
use binary search
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class test:
    def find_index(nums, target):
        low, high = 0, len(nums) - 1
        #mid = (low+high) // 2
        #mid_number = nums[mid]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[low] <= nums[mid]:
                # target is greater than middle or less than the left most value
                # example if target was 5 -> [6, 7, 8, 2, 5]
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else: # target is less than middle but greater than leftmost value
                    high = mid - 1

            # right sorted portion
            else:
                # if mid_number > target:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
         
nums = [4,5,6,7,0,1,2]
target = 0
t = test.find_index(nums, target)
print (t)