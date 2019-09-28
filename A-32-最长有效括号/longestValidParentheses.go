package main

import "fmt"

func main() {
	result := longestValidParentheses("(())")
	fmt.Println(result)
}
func longestValidParentheses(s string) int {
	var itemList []int
	j := 0
	res := 0
	for i, item := range s {
		if string(item) == "(" {
			itemList = append(itemList, i)
		} else {
			if len(itemList) == 0 {
				j = i + 1
				continue
			} else {
				itemList = itemList[:len(itemList)-1]
				if len(itemList) == 0 {
					res = MaxItem(res, i-j+1)
				} else {
					res = MaxItem(res, i-itemList[len(itemList)-1])
				}

			}
		}
	}
	return res
}

func MaxItem(x, y int) int {
	if x >= y {
		return x
	}
	return y
}
