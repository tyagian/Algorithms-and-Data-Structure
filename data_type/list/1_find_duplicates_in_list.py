from collections import Counter
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]
counts = dict(Counter(numbers))
duplicates = {key:value for key, value in counts.items() if value > 1}
print (duplicates)

"""
# First approach: add count of all elements
l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
# sort elements, {k:v for (k,v) in dict.items() if v > something}
duplicate_elements = {k:v for (k,v) in d.items() if v > 1}
print (duplicate_elements)
"""