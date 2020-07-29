""" Para a text and return top n words used with the number of  times the word appeared.
https://leetcode.com/problems/top-k-frequent-words/discuss/547015/Python-3-Sort-Heap-Trie
""" """ #Case1:
from collections import Counter
data_set = "Welcome to the world of Geeks. This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks."
# split() returns list of all the words in the string 
split_it = data_set.split() 
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it)   
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(4) 
print(most_occur) """
#Approach 2: Heap. Time Complexity, O(N) to build a heap, O(klogN) to find the pop the first kth largest elements and reconstruct the heap.
import collections
import heapq
#from collections import Counter
class Solution:
    def topKFrequent(words,k):
        word_s = words.split() #.replace(",","").lower()
        print (word_s)
        words = [sub.replace(' ', '').replace(".","").replace(",","") for sub in word_s] 
        count = collections.Counter(words)
        #print (type(count))
        #print (count)
        heap = [(-freq, word) for word, freq in count.items()]
        #print (type(heap))
        #print (("\nheap", heap))
        heapq.heapify(heap)
        return [heapq.heappop(heap) for _ in range(k)]
words = "Welcome welcome, to the world of Geeks. This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks."
#words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print (Solution.topKFrequent(words,4))
# Time: O(N) to build a heap, O(klogN) to find the pop the first kth largest elements and reconstruct the heap.
# Space: 
###############################################
"""
$ python3 2_freq_words.py 
<class 'collections.Counter'>
Counter({'to': 4, 'and': 4, 'Geeks': 4, 'well': 3, 'for': 3, 'your': 3, 'article': 3, 'the': 2, 'of': 2, 'Geeks.': 2, 'like': 2, 'contribute': 2, 'Welcome': 1, 'world': 1, 'This': 1, 'portal': 1, 'has': 1, 'been': 1, 'created': 1, 'provide': 1, 'written': 1, 'thought': 1, 'explained': 1, 'solutions': 1, 'selected': 1, 'questions': 1, 'If': 1, 'you': 1, 'would': 1, 'here': 1, 'is': 1, 'chance': 1, 'You': 1, 'can': 1, 'write': 1, 'mail': 1, 'at': 1, 'geeksforgeeks': 1, 'org': 1, 'See': 1, 'appearing': 1, 'on': 1, 'main': 1, 'page': 1, 'help': 1, 'thousands': 1, 'other': 1})
<class 'list'>
[(-1, 'Welcome'), (-4, 'to'), (-2, 'the'), (-1, 'world'), (-2, 'of'), (-2, 'Geeks.'), (-1, 'This'), (-1, 'portal'), (-1, 'has'), (-1, 'been'), (-1, 'created'), (-1, 'provide'), (-3, 'well'), (-1, 'written'), (-1, 'thought'), (-4, 'and'), (-1, 'explained'), (-1, 'solutions'), (-3, 'for'), (-1, 'selected'), (-1, 'questions'), (-1, 'If'), (-1, 'you'), (-2, 'like'), (-4, 'Geeks'), (-1, 'would'), (-2, 'contribute'), (-1, 'here'), (-1, 'is'), (-3, 'your'), (-1, 'chance'), (-1, 'You'), (-1, 'can'), (-1, 'write'), (-3, 'article'), (-1, 'mail'), (-1, 'at'), (-1, 'geeksforgeeks'), (-1, 'org'), (-1, 'See'), (-1, 'appearing'), (-1, 'on'), (-1, 'main'), (-1, 'page'), (-1, 'help'), (-1, 'thousands'), (-1, 'other')]
['Geeks', 'and', 'to', 'article']
"""