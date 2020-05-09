class Solution:
    #def __init__(self, email_id):
    #    self.emails = email_id
    def findNumbers(self, nums: List[int]) -> int:
        output = 0 
        for i in nums:
            p = i.split()
            if n in p%2 == 0:
                output += 1
            else:
                pass
    return output
A = input_array([12,345,2,6,7896])
print (A.findNumbers())