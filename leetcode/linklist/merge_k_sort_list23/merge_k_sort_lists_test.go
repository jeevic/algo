package merge_k_sort_list23

import "testing"

type Question struct {
	Input  [][]int
	Output []int
}

func InitListNode(l []int) *ListNode {
	if len(l) < 1 {
		return nil
	}

	Ln := new(ListNode)
	Ln.Val = l[0]
	cur := Ln

	for i := 1; i < len(l); i++ {
		tempNode := new(ListNode)
		tempNode.Val = l[i]
		cur.Next = tempNode
		cur = cur.Next
	}

	return Ln
}

var qs = []Question{
	{
		[][]int{
			{1, 4, 5},
			{1, 3, 4},
			{2, 6},
		},
		[]int{1, 1, 2, 3, 4, 4, 5, 6},
	},
	{
		[][]int{},
		[]int{},
	},
	{
		[][]int{
			{},
		},
		[]int{},
	},
}

func TestMergeKLists(t *testing.T) {
	for _, q := range qs {
		var lists = make([]*ListNode, 0, 1)
		for _, l := range q.Input {
			ln := InitListNode(l)
			lists = append(lists, ln)
		}

		l3 := MergeKLists(lists)
		if SliceForEqual(ListNodeToSlice(l3), q.Output) {
			t.Logf("input:%#v   result:%#v match ", q.Input, ListNodeToSlice(l3))
		} else {
			t.Errorf("[error]input:%#v  result:%#v not match", q.Input, ListNodeToSlice(l3))
		}
	}
}

func ListNodeToSlice(l *ListNode) []int {
	ret := make([]int, 0, 1)
	for l != nil {
		ret = append(ret, l.Val)
		l = l.Next
	}
	return ret
}

func SliceForEqual(s1 []int, s2 []int) bool {
	if len(s1) != len(s2) {
		return false
	}

	if (s1 == nil) != (s2 == nil) {
		return false
	}

	for i, v := range s1 {
		if v != s2[i] {
			return false
		}
	}

	return true
}
