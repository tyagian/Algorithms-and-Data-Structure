# 4. Removing Redundancy
# Question: Identify and eliminate redundancy in the code.
def greet(name):
    print("Hello, " + name + "!")
    return "Hello, " + name + "!"
result = greet("Alice")
print(result)

# Refactored Solution:
def greet(name):
    greeting = "Hello, " + name + "!"
    print(greeting)
    return greeting

result = greet("Alice")
print(result)


