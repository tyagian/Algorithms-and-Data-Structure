"""
# Find duplicate elements in list:
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
unique_elements = {k:v for (k,v) in d.items() if v < 2}
print ("duplicate_elements:",duplicate_elements)
print ("unique_elements:",unique_elements)
"""
"""
# Using Collections as counter
from collections import Counter
l = [1,2,3,4,5,1,3,4,5,1,1,1,1]
counts = dict(Counter(l))
dup_elements = {k:v for (k,v) in counts.items() if v > 1}
unique_elements = {k:v for (k,v) in counts.items() if v < 2}
print ("duplicate_elements:",dup_elements)
print ("unique_elements:",unique_elements)
"""