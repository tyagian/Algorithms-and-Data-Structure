#6. Finding Minimum and Maximum Without Built-in Functions:
#Question: Implement functions to find the minimum and maximum elements in a list without using built-in functions like min() and max().

def find_min(nums):
    if not nums:
        return None
    minimum = nums[0]
    for num in nums[1:]:
        if num < minimum:
            minimum = num
    return minimum

def find_max(nums):
    if not nums:
        return None
    maximum = nums[0]
    for num in nums[1:]:
        if num > maximum:
            maximum = num
    return maximum