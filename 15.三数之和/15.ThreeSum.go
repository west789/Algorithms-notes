package main

import (
	"fmt"
	"sort"
)

func main() {
	array := []int{-1, 0, 1, 2, -1, -4}
	res := ThreeSum(array)
	fmt.Println(res)
}

// ThreeSum Get sum of three numbers
func ThreeSum(nums []int) [][]int {
	sort.Ints(nums)
	result := [][]int{}
	for i := 0; i < len(nums)-1; i++ {
		j := i + 1
		z := len(nums) - 1
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		for j < z {
			if nums[i]+nums[j]+nums[z] < 0 {
				j++
			} else if nums[i]+nums[j]+nums[z] > 0 {
				z--
			} else {
				item := []int{nums[i], nums[j], nums[z]}
				result = append(result, item)
				for j < z && nums[j] == nums[j+1] {
					j++
				}
				for j < z && nums[z] == nums[z-1] {
					z--
				}
				j++
				z--
			}
		}
	}
	return result
}
