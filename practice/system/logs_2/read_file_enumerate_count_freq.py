#https://stackabuse.com/read-a-file-line-by-line-in-python/#readafilelinebylinewithaforloopmostpythonicapproach

"""
To read line by line without loading file in memory
with open('Iliad.txt') as f:
    for index, line in enumerate(f):
        print("Line {}: {}".format(index, line.strip()))
"""
"""
You can write a from-scratch solution to count the frequency of certain words, without using 
any external libraries. Let's write a simple script that loads in a file, reads it line-by-line 
and counts the frequency of words, printing the 10 most frequent words and the number of their 
occurrences
"""
import sys, os
def order_bag_of_words(bag_of_words, desc=False):
    words = [(word, cnt) for word, cnt in bag_of_words.items()]
    return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1    
def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print ("File path {} doesn't exit. Exiting....".format(filepath))
        sys.exit()
    bag_of_words = {}
    with open(filepath) as fp:
        for line in fp:
            record_word_cnt(line.strip().split(' '), bag_of_words)
    sorted_words = order_bag_of_words(bag_of_words, desc= True)
    print("Most frequent 10 words {}".format(sorted_words[:10]))
if __name__ == '__main__':
    main()