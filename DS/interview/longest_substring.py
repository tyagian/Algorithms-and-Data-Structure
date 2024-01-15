#  Longest Substring Without Repeating Characters
# Find the length of the longest substring without repeating characters 
# in a given string.

def longest_substring_without_repeating(s):
    char_index_map = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# Example
print(longest_substring_without_repeating("abcabcbb"))  # Output: 3
