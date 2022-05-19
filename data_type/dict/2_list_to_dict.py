#1. Convert a list to a dictionary 2_listwith key as the item and value as the count of the item
#https://www.scaler.com/topics/list-to-dictionary-python/


#We can use Counter(), zip(), and enumerate() method, for our conversion from list to dictionary.

#simple approach
l = ['apple','red','apple','red','red','pear']
dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print (dic)
# Sort dictionary elements
#for i in sorted(dic, key=dic.get):
#    print (i, dic[i])

# print duplicates
# {k:v for (k,v) in dict.items() if v > something}
duplicate_elements = {k:v for (k,v) in d.items() if v > 1}
#print (duplicate_elements)

# sort by key
for i in sorted(dic.keys()):
    print (i, dic[i])
    
# sort by value
print (sorted(dic.items(), key= lambda kv: (kv[1], kv[0])))
#Output
#{'apple': 2, 'red': 3, 'pear': 1}
#pear 1
#apple 2
#red 3

"""
l = ['apple','red','apple','red','red','pear']
from collections import defaultdict
#d = defaultdict(int)
d = {}
for i in l:
    d[i] += 1
print (d)
"""

"""
# Using collections
from collections import Counter
l = ['apple','red','apple','red','red','pear']
dic = Counter(l)
#>>> Counter(['apple','red','apple','red','red','pear'])
#Counter({'red': 3, 'apple': 2, 'pear': 1})
"""
"""
a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5,2, 3, 4, 5,3, 4, 5]
dic = {}
for i in range(len(a)):
    dic[a[i]] = a.count(a[i])
print (dic)
"""
