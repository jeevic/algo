package permutations48

import (
	"testing"
)

type Question struct {
	Input  []int
	Output [][]int
}

var questions []Question = []Question{
	{[]int{1, 2, 3}, [][]int{
		{1, 2, 3},
		{1, 3, 2},
		{2, 1, 3},
		{2, 3, 1},
		{3, 1, 2},
		{3, 2, 1},
	}},
	{
		[]int{0, 1},
		[][]int{{0, 1}, {1, 0}},
	},
	{
		[]int{1},
		[][]int{{1}},
	},
}

func equal(a, b [][]int) {

}

func TestPermute(t *testing.T) {
	for _, q := range questions {
		output := Permute(q.Input)
		t.Logf("comput output:%#v", output)
		t.Logf("out put: %#v", q.Output)

	}
}

func TestPermuteTrack(t *testing.T) {
	for _, q := range questions {
		output := PermuteTrack(q.Input)
		t.Logf("comput output:%#v", output)
		t.Logf("out put: %#v", q.Output)

	}
}
