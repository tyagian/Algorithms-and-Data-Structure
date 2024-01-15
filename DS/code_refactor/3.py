# Improving Function Modularity:
# Question: Refactor the code to improve modularity.

def calculate_area(radius):
    return 3.14 * radius * radius

def calculate_volume(radius, height):
    base_area = 3.14 * radius * radius
    return base_area * height

# refactor

def calculate_circle_area(radius):
    return 3.14 * radius * radius

def calculate_cylinder_volume(radius, height):
    return calculate_circle_area(radius) * height
