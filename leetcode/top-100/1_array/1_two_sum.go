package main

import "fmt"

func main() {
	num := []int{2, 7, 11, 15}
	fmt.Println(twosum(num, 9))
}

func twosum(array []int, target int) []int {
	for i := 0; i < len(array)-1; i++ {
		for j := i + 1; j < len(array); j++ {
			if array[i]+array[j] == target {
				return []int{array[i], array[j]}
			}
		}
	}
	return []int{}
}
