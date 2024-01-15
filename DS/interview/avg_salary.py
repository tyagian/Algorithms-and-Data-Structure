# Calculate Average Salary Excluding Minimum and Maximum
# Given a list of salaries, calculate the average salary excluding 
# the minimum and maximum salaries.

def average_salary(salaries):
    if len(salaries) <= 2:
        return 0
    
    salaries.sort()
    return sum(salaries[1:-1]) / (len(salaries) - 2)

# Example
salary_list = [6000, 5000, 7000, 8000, 1000]
print(average_salary(salary_list))  # Output: 6500.0

