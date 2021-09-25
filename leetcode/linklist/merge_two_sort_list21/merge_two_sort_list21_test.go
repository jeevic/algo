package merge_two_sort_list21

import "testing"

type Question struct {
	Input struct {
		List1 []int
		List2 []int
	}
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

	{struct {
		List1 []int
		List2 []int
	}{
		[]int{1, 2, 4}, []int{1, 3, 4},
	},
		[]int{1, 1, 2, 3, 4, 4},
	},
	{struct {
		List1 []int
		List2 []int
	}{
		[]int{}, []int{},
	},
		[]int{},
	},

	{struct {
		List1 []int
		List2 []int
	}{
		[]int{}, []int{0},
	},
		[]int{0},
	},
}

func TestMergeTwoLists(t *testing.T) {
	for _, q := range qs {
		l1 := InitListNode(q.Input.List1)
		l2 := InitListNode(q.Input.List2)
		l3 := MergeTwoLists(l1, l2)
		if SliceForEqual(ListNodeToSlice(l3), q.Output) {
			t.Logf("input:%#v %#v  result:%#v match ", q.Input.List1, q.Input.List2, ListNodeToSlice(l3))
		} else {
			t.Errorf("[error]input:%#v %#v result:%#v not match", q.Input.List1, q.Input.List2, ListNodeToSlice(l3))
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
