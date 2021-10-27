package binarySearch_704

//@see  https://leetcode-cn.com/problems/binary-search/

func BinarySearch(nums []int, target int) int {
	length := len(nums)
	if length < 1 {
		return -1
	}
	left, right := 0, length-1

	for left <= right { // [left + 1, left]
		mid := left + (right-left)/2
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		}
	}

	return -1
}
