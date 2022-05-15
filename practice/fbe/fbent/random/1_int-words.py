"""
Given Integer, translate it into English words, i.e . 432,000 -> four hundred thirty two thousands. 
Another question is very straightforward: Given an array and an integer z, rotate the array starting 
from index z to the front, i.e. 
['a', 'b', 'c', 'd', 'e', 'f', 'g'] z=3 => ['e', 'f', 'g', 'a', 'b', 'c', 'd']
"""
class Solution:
    def numberToWords(self,num):
        if num==0: return 'Zero'
        w_unit= ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        w_ten=['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        unit = num % 10
        ten = (num//10) % 10
        hundred = (num//100) % 10
        thousand = (num//1000) % 1000
        million = (num//10**6) % 1000
        billion = (num//10**9) % 1000

        word = w_unit[ten*10+unit] if ten==1 else w_unit[unit]
        if ten>1:
            word = w_ten[ten]+' '+word
        if hundred: word = w_unit[hundred]+' Hundred '+word
        if thousand: word = numberToWords(thousand)+' Thousand '+word
        if million: word = numberToWords(million)+' Million '+word
        if billion: word = numberToWords(billion)+' Billion '+word
        return word.strip()

print (Solution.numberToWords(1234567891))