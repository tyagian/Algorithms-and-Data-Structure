#Question: Simplify the following nested conditional statements.
def check_number(x):
    if x > 0:
        if x % 2 == 0:
            return "Positive and Even"
        else:
            return "Positive and Odd"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

# Refactored Solution:
def check_number(x):
    if x > 0:
        return "Positive and Even" if x % 2 == 0 else "Positive and Odd"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"


