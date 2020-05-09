## case1
def twoNumberSum(array, targetSum):
    # Write your code here.
	# Time: O(n), Space: O(n)
    nums = {}
	for num in array:
		potential_match = targetSum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums[num] = True
	return []

## case2
def twoNumberSum(array, targetSum):
    # Write your code here.
	# Time: O(n), Space: O(n)
    nums = {}
	for num in array:
		potential_match = targetSum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums[num] = True
	return []

## case3
def twoNumberSum(array, targetSum):
    # Write your code here.
	# Time: O(n), Space: O(n)
    nums = {}
	for num in array:
		potential_match = targetSum - num
		if potential_match in nums:
			return [potential_match, num]
		else:
			nums[num] = True
	return []
