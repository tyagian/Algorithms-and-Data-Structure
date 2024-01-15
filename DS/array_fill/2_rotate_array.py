#Rotate Array:
#Question: Rotate an array to the right by k steps.

def rotate_array(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

