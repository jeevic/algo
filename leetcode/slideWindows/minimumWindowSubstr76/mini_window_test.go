package minimumWindowSubstr76

import "testing"

func TestMinWindow(t *testing.T) {
	str := "aaaaaaaaaaaabbbbbcdd"
	target := "abcdd"

	expire := "abbbbbcdd"

	if MinWindow(str, target) == expire {
		t.Log("expire")
	} else {
		t.Error("not expire")
	}
}
