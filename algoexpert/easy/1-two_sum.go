/*
package main
// O(n^2) time | O(1) space
func TwoNumberSum(array []int, target int) []int {
	// Write your code here.

	for i :=0; i < len(array)-1; i++ {
		for j :=i+1; j < len(array); j++ {			
			if array[i] + array[j] == target {
				return []int{ array[i], array[j]}
			}
		}
	}

	return []int{}
}

// Case2: 


// Case3: 
package main
func TwoNumberSum(array []int, target int) []int {
	// Write your code here.
	for i :=0; i < len(array)-1; i++ {
		for j :=i+1; j < len(array); j++ {			
			if array[i] + array[j] == target {
				return []int{ array[i], array[j]}
			}
		}
	}

	return []int{}
}

/*