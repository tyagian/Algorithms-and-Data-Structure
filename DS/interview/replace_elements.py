# Question: Replace Elements with Greatest Element on Right Side
# Given an array, replace each element with the greatest element 
# among the elements to its right, and replace the last element with -1.
def replace_elements(arr):
    max_right = -1

    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_right
        max_right = max(max_right, temp)

# Example
array = [17, 18, 5, 4, 6, 1]
replace_elements(array)
print(array)  # Output: [18, 6, 6, 6, 1, -1]
