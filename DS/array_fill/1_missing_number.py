#Question: Given an array containing n distinct numbers taken from the range 0 to n, find the one missing number.

def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum