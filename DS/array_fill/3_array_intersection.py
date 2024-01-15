#Array Intersection:
#Question: Find the intersection of two arrays.

def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))
