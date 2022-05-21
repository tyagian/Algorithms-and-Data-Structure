
"""
Find min in rotated sorted array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
memory: O(log n) since binary search used
"""
class test:

    def find_min(arr):
        low, high = 0, len(arr) - 1

        if arr[low] <= arr[high]:
            return arr[low]

        while low <= high:
            if low == high:
                return low
            mid = (low+high) // 2
            print (f"low, high, mid: {low}, {high}, {mid} and {arr[mid]}")
            if mid < high and arr[mid+1] < arr[mid]:
                return arr[mid+1]
            if mid > low and arr[mid] < arr[mid-1]:
                return arr[mid]
            if arr[mid] < arr[high]:
                high = mid-1
            else:
                low = mid + 1
 
arr = [4,5,6,7,-1,0,1,2]
t = test.find_min(arr)
print (t)