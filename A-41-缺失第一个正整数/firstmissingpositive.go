package main

import "fmt"

// in_array is like python's in
func inArray(val int, array []int) (exists bool, index int) {
	exists = false
	index = -1

	for i, v := range array {
		if val == v {
			index = i
			exists = true
			return
		}
	}

	return
}

//第一种解法，多增加了一个函数
func firstMissingPositive(nums []int) int {
	var n int
	n = 1
	for {
		exists, _ := inArray(n, nums)
		if exists {
			n++
		} else {
			break
		}
	}
	return n
}

//第二种解法
func firstMissingPositive1(nums []int) int {
	for i := 0; i < len(nums); {
		// fmt.Println(nums[nums[i]-1])
		if nums[i] > 0 && nums[i] <= len(nums) && nums[nums[i]-1] != nums[i] {
			nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
		} else {
			i++
		}
	}
	fmt.Println(nums)
	for i := 0; i < len(nums); i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}
	return len(nums) + 1
}
func main() {
	// names := []string{"Mary", "Anna", "Beth", "Johnny", "Beth"}
	nums := []int{-1, -3, -2, 2}
	fmt.Println(firstMissingPositive(nums))
	fmt.Println("--------------------------")
	fmt.Println(firstMissingPositive1(nums))
	// fmt.Println(inArray("Jack", names))
}
