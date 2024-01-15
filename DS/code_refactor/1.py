"""
1. Refactoring for Readability:
Question: Refactor the following code for improved readability.
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count
"""
"""
Refactored Solution:
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
"""