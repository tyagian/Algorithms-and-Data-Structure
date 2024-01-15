#Given a list of strings, group anagrams together.

from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())

# Example
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(word_list))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
