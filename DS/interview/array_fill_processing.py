# Array Fill and Processing:
# Question: Rotate Array
# Rotate an array to the right by k steps
def rotate_array(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# Example
arr = [1, 2, 3, 4, 5]
rotate_array(arr, 2)
print(arr)  # Output: [4, 5, 1, 2, 3]
