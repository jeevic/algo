package minimumWindowSubstr76

//@see https://leetcode-cn.com/problems/minimum-window-substring/submissions/

func MinWindow(s string, t string) string {
	slen := len(s)
	if slen == 0 || len(t) == 0 {
		return ""
	}

	var windows, needs = make(map[string]int), make(map[string]int)
	//record needs bytes  count
	for _, v := range t {
		if _, ok := needs[string(v)]; !ok {
			needs[string(v)] = 1
		} else {
			needs[string(v)]++
		}
	}
	//窗口指针
	left, right := 0, 0
	rleft := 0
	rlen := slen + 1
	//验证
	valid := 0
	srune := []rune(s)
	for right < slen {
		char := string(srune[right])
		//记录数量
		if _, ok := windows[char]; ok {
			windows[char]++
		} else {
			windows[char] = 1
		}

		right++

		//判断
		if _, ok := needs[char]; ok && needs[char] == windows[char] {
			valid++
		}

		for valid == len(needs) {
			if right-left <= rlen {
				rleft = left
				rlen = right - left
			}

			char2 := string(srune[left])
			windows[char2]--
			if _, ok := needs[char2]; ok && needs[char2] > windows[char2] {
				valid--
			}
			left++
		}
	}

	if rlen == slen+1 {
		return ""
	}
	return string(srune[rleft : rleft+rlen])
}
