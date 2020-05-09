"""
Check if there is a set of 3 elements in an integer array , that adds upto zero?
https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
"""
def findTriplets(arr, n): 
    found = False
    for i in range(n - 1): 
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j]) 
    if found == False: 
        print("No Triplet Found")
    return ''
arr = [0, -1, 2, -3, 1] 
n = len(arr) 
print (findTriplets(arr, n))