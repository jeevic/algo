package binary_search

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

func LeftBoundBinarySearch(nums []int, target int) int {
	length := len(nums)
	if length < 1 {
		return -1
	}
	left, right := 0, length-1

	for left <= right { // [left + 1, left]
		mid := left + (right-left)/2
		if nums[mid] == target {
			right = mid - 1
		} else if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		}
	}
	if left >= length || nums[left] != target {
		return -1
	}
	return left
}

func RightBoundBinarySearch(nums []int, target int) int {
	length := len(nums)
	if length < 1 {
		return -1
	}
	left, right := 0, length-1

	for left <= right { // [left + 1, left]
		mid := left + (right-left)/2
		if nums[mid] == target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		}
	}
	if left >= length || nums[left-1] != target {
		return -1
	}
	return left - 1
}

//左闭右开法

func BinarySearch1(nums []int, target int) int {
	length := len(nums)
	left, right := 0, length

	for left < right { //[left, left)
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

func LeftBoundBinarySearch1(nums []int, target int) int {
	length := len(nums)
	left, right := 0, length

	for left < right { //[left, left)
		mid := left + (right-left)/2
		if nums[mid] == target {
			right = mid
		} else if nums[mid] > target {
			right = mid
		} else if nums[mid] < target {
			left = mid + 1
		}
	}

	if left >= length || nums[left] != target {
		return -1
	}
	return left
}

func RightBoundBinarySearch1(nums []int, target int) int {
	length := len(nums)
	if length < 1 {
		return -1
	}
	left, right := 0, length

	for left < right { // [left + 1, left)
		mid := left + (right-left)/2
		if nums[mid] == target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid
		} else if nums[mid] < target {
			left = mid + 1
		}
	}
	if left >= length || nums[left-1] != target {
		return -1
	}
	return left - 1
}
