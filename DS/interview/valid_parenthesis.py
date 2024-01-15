# Valid Parentheses
#Write a function to determine if a given string containing parentheses is valid.

def is_valid_parentheses(s):
    stack = []
    parentheses_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        print (char)
        if char in parentheses_mapping.values():
            stack.append(char)
        elif char in parentheses_mapping.keys():
            if not stack or stack.pop() != parentheses_mapping[char]:
                return False

    return not stack

# Example
print(is_valid_parentheses("(){}[]"))  # Output: True

