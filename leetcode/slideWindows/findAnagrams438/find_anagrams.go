package findAnagrams438

//@see  https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
// 438. 找到字符串中所有字母异位词
// middle

func findAnagrams(s string, p string) []int {
	sLen, pLen := len(s), len(p)
	if sLen <= 0 || pLen <= 0 {
		return nil
	}

	var result = make([]int, 0, 1)
	var left, right = 0, 0
	var valid = 0
	var windows, needs = make(map[rune]int), make(map[rune]int)
	for _, rn := range p {
		if _, ok := needs[rn]; ok {
			needs[rn]++
		} else {
			needs[rn] = 1
		}
	}

	sRune := []rune(s)
	for right < sLen {
		char := sRune[right]
		right++
		if _, ok := windows[char]; ok {
			windows[char]++
		} else {
			windows[char] = 1
		}

		if _, ok := needs[char]; ok {
			if windows[char] == needs[char] {
				valid++
			}
		}

		for valid == len(needs) {
			if right-left == len(p) {
				result = append(result, left)
			}
			char2 := sRune[left]
			left++
			windows[char2]--
			if _, ok := needs[char2]; ok {
				if windows[char2] < needs[char2] {
					valid--
				}
			}
		}

	}
	return result
}
