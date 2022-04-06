package lengthOfLongestSubstring3

//@see https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
// 3. 无重复字符的最长子串

func lengthOfLongestSubstring1(s string) int {
	var result = 0
	sRune := []rune(s)
	for cursor1 := 0; cursor1 < len(sRune); cursor1++ {
		var windows = make(map[rune]int)
		for cursor2 := cursor1; cursor2 < len(sRune); cursor2++ {
			char := sRune[cursor2]
			if _, ok := windows[char]; !ok {
				 windows[char] = 1
				 if cursor2 - cursor1 + 1 > result {
				 	result = cursor2 - cursor1 + 1
				 }
			} else {
				break
			}
		}
	}
	return result

}


func lengthOfLongestSubstring(s string) int {
	sLen := len(s)
	if sLen <=  0 {
		return 0
	}

	var left, right = 0, 0
	var result = 0
	var windows  = make(map[rune]int)
	sRune := []rune(s)
	for right < sLen {
		char := sRune[right]
		right++
		if _, ok := windows[char]; !ok || windows[char] == 0{
			windows[char] = 1
			if right - left > result {
				result = right - left
			}
		} else {
			windows[char]++
			//去掉 char
			for left <= right {
				char2 := sRune[left]
				left++
				windows[char2]--
				if char2 == char {
					break
				}
			}
		}

	}
	return result
}