package permutationInString576

func checkInclusion(s1 string, s2 string) bool {
	s1len, s2len := len(s1), len(s2)
	if s1len <= 0 || s2len <= 0 {
		return false
	}
	var windows, needs = make(map[rune]int), make(map[rune]int)
	for _, rn := range s1 {
		if _, ok := needs[rn]; ok {
			needs[rn]++
		} else {
			needs[rn] = 1
		}
	}

	var left, right = 0, 0
	valid := 0
	s2Rune := []rune(s2)
	for right < s2len {
		char := s2Rune[right]
		right++

		if _, ok := windows[char]; ok {
			windows[char]++
		} else {
			windows[char] = 1
		}
		if _, ok := needs[char]; ok {
			if needs[char] == windows[char] {
				valid++
			}
		}

		for valid == len(needs) {
			if right-left == len(s1) {
				return true
			}
			char2 := s2Rune[left]
			left++
			windows[char2]--
			if _, ok := needs[char2]; ok {
				if needs[char2] > windows[char2] {
					valid--
				}
			}
		}
	}
	return false
}
