# Write a program to create a dictionary that contains number as its key, 
#and square of that number as its value.
"""
Input: Enter a number
Output:
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
"""
# Take an input n = 10, output should show 1-10 and squares of those numbers
"""
# Abstracting complexity in functions
class n_square():
    def __init__(self,numbers):
        self.numbers = numbers
        self.sq_number = {i : i**2 for i in range(0, numbers+1)}

    def output(self):
        #sq_number = {i : i**2 for i in range(0,numbers+1)}
        return f"These are squares of numbers from 0 to {self.numbers}: {self.sq_number}"
        
def main():
    numbers = int(input())
    n = n_square(numbers) 
    print (n.output())
if __name__ == '__main__':
    main()
"""
"""
# Other way just to returning values in function and format output in main()
class calculate():
    def __init__(self,numbers):
        self.numbers = numbers
        
    def sq(self):
        result = {i : i**2 for i in range(0,self.numbers+1)}
        return result
        
def main():
    print ("Enter the max number to get squares")
    num = int(input("Entered number is: "))
    
    n = calculate(num)
    print (f"These are squares of numbers from 0 to {num}: {n.sq()}") 
    
if __name__ == '__main__':
    main()

"""