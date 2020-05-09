package main

import (
	"fmt"
)

func getSum(a int, b int) int {
	var carry int
	for b != 0 {
		carry = a & b
		a = a ^ b
		b = carry << 1
	}
	return a
}

func main() {
	a, b := 10, 15
	test := getSum(a, b)
	fmt.Println(test)
}
