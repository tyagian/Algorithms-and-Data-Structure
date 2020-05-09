"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
package main
import (
	"fmt"
)
func productExceptSelf(nums []int) []int {
    forward := make([]int, len(nums))
    backward := make([]int, len(nums))
    ans := make([]int, len(nums))
    // Set value of each element as 1, for multiplication
    for i := range nums {
        forward[i], backward[i] = 1, 1
    }
    // Value of forward at i is equal to previous index * nums at previous index
    // Skipping first element, because it shouldn't multiply with itself
    for i := 1; i < len(nums); i++ {
        forward[i] = forward[i-1] * nums[i-1]
    }
    // Value of backward is equal to previous index * nums at previous index
    // Counting backwards, skipping last element because it shouldn't multiply with itself
    for i := len(nums)-2; i >= 0; i-- {
        backward[i] = backward[i+1] * nums[i+1]
    }
    // Values at each index of forward and backward can multiply with each other
    for i := range nums {
        ans[i] = forward[i] * backward[i]
    }
    return ans
}


func main() {
	a := [1,2,3,4]
	test := productExceptSelf(a)
	fmt.Println(test)
}
