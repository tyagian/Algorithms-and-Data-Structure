"""
Write a bash script to calculate the frequency of each word in a text file words.txt.
For simplicity sake, you may assume:
words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
Example:
Assume that words.txt has the following content:
the day is sunny the the
the sunny is is
Your script should output the following, sorted by descending frequency:
the 4
is 3
sunny 2
day 1
Note: Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
Could you write it in one-line using Unix pipes?
"""
"""
import datetime
begin_time = datetime.datetime.now()
d = {}
with open("5_sample.txt") as file:
    for line in file:
        line = line.strip().lower().split(" ")
        for word in line:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
print (d)
print(datetime.datetime.now() - begin_time)
#for key, value in d.items():
#    print (key, ":", value)
"""
from collections import defaultdict
import datetime
word_count = defaultdict(int)
begin_time = datetime.datetime.now()
#d = {}
with open("5_sample.txt") as file:
    for line in file:
        line = line.strip().lower().split(" ")
        for word in line:
            word_count[word] += 1
print (word_count)
print(datetime.datetime.now() - begin_time)
