package permutations48

/**
 * 解法思路:
 * 1、自顶而下选择排列 i 位置, 在自底而上拼接上 i 位置数
 */
func Permute(nums []int) [][]int {
	length := len(nums)
	var result = make([][]int, 0, length)
	if length == 1 {
		result = append(result, nums)
		return result
	}
	for i := 0; i < length; i++ {
		val := nums[i]
		var sumNums = make([]int, 0, length-1)
		if i == 0 {
			sumNums = nums[1:]
		} else if i == length-1 {
			sumNums = nums[0 : length-1]
		} else {
			sumNums = append(sumNums, nums[0:i]...)
			sumNums = append(sumNums, nums[i+1:]...)
		}
		subRes := Permute(sumNums)
		for j := 0; j < len(subRes); j++ {
			result = append(result, append([]int{val}, subRes[j]...))
		}
	}
	return result
}

func PermuteTrack(nums []int) [][]int {
	var res = make([][]int, 0, 1)
	var track = make([]int, 0, len(nums))
	backTrace(nums, track, &res)
	return res
}

func backTrace(nums []int, track []int, res *[][]int) {
	if len(track) == len(nums) {
		//必需赋值
		copy := CopySlice(track)
		*res = append(*res, copy)
		return
	}
	for _, item := range nums {
		if contain(item, track) {
			continue
		}
		track = append(track, item)
		backTrace(nums, track, res)
		track = track[0 : len(track)-1]
	}
}

func contain(val int, items []int) bool {
	for _, item := range items {
		if val == item {
			return true
		}
	}
	return false
}

func CopySlice(slice []int) []int {
	copy := make([]int, len(slice))
	for index, item := range slice {
		copy[index] = item
	}
	return copy
}
