#2. Maximum Occurring Element:
#Question: Find the element with the highest occurrence in a list.
from collections import Counter

def most_common_element(nums):
    count_dict = Counter(nums)
    print (count_dict)
    return max(count_dict, key=count_dict.get)
print (most_common_element([4,5,6,3,1,1,3,9]))