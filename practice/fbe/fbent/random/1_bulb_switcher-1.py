"""There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every third 
bulb (turning on if it's off or turning off if it's on). For the i-th round, you 
toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how 
many bulbs are on after n rounds.
Example: Input: 3, Output: 1 
Explanation: At first, the three bulbs are [off, off, off]. After first round, the 
three bulbs are [on, on, on]. After second round, the three bulbs are [on, off, on]. 
After third round, the three bulbs are [on, off, off]. So you should return 1, because 
there is only one bulb is on.
https://leetcode.com/problems/bulb-switcher/discuss/485178/Python-3-solutions-O(1)-fastest-O(1)-generalized-for-a-b-with-explanation.
"""

def bulb_switcher(num):
    n = len(num)
    #for i in range(1,n):
    #    num[i] = "off"
    return (n**0.5)

print (bulb_switcher(["on", "on", "on","on", "on", "on"]))