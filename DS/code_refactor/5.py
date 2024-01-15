#Question: Refactor the code using list comprehensions.
def filter_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# refactor
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


