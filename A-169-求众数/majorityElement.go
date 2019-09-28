package main

import (
	"fmt"
	"sort"
)

func majorityElement(nums []int) int {
	sort.Ints(nums)
	return nums[(len(nums) / 2)]

	//摩尔投票法
	// if len(nums) == 0 {
	// 	return 0
	// }

	// i, res := 1, nums[0]

	// for _, v := range nums[1:] {
	// 	if v != res {
	// 		i--
	// 	} else {
	// 		i++
	// 	}
	// 	fmt.Println("此时i", i)
	// 	if i <= 0 {
	// 		res = v
	// 		i = 1
	// 	}
	// }

	// return res
}

func main() {
	res := majorityElement([]int{1, 2, 2, 1, 2, 2, 1})
	fmt.Println(res)
}
