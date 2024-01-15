# Decode String
# Given a string encoded with a certain pattern, decode it
def decode_string(s):
    stack = []

    for char in s:
        if char.isdigit():
            stack.append(int(char))
        elif char == '[':
            stack.append('')
        elif char == ']':
            substring = stack.pop()
            count = stack.pop()
            stack[-1] += substring * count
        else:
            stack[-1] += char

    return ''.join(stack)

# Example
print(decode_string("3[a]2[bc]"))  # Output: "aaabcbc"
