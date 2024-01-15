# Word Break: Given a string and a dictionary of words, determine if the string 
# can be segmented into a space-separated sequence of dictionary words.

def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[-1]

# Example
word_dict = ["apple", "pen"]
print(word_break("applepenapple", word_dict))  # Output: True
