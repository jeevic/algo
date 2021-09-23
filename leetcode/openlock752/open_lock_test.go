package openlock752

import "testing"

type Question struct {
	Input  Input
	Output int
}

type Input struct {
	Deadends []string
	Target   string
}

var qs = []Question{
	{Input: Input{Deadends: []string{"0201", "0101", "0102", "1212", "2002"}, Target: "0202"}, Output: 6},
	{Input: Input{Deadends: []string{"8888"}, Target: "0009"}, Output: 1},
	{Input: Input{Deadends: []string{"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"}, Target: "8888"}, Output: -1},
	{Input: Input{Deadends: []string{"0000"}, Target: "8888"}, Output: -1},
}

func TestOpenLock(t *testing.T) {
	for _, q := range qs {
		step := OpenLock(q.Input.Deadends, q.Input.Target)
		if step == q.Output {
			t.Logf("input:%v output:%d match step:%d", q.Input, q.Output, step)
		} else {
			t.Errorf("[error]input:%v output:%d not match step:%d", q.Input, q.Output, step)
		}
	}
}
