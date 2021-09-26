package merge_k_sort_list23

type ListNode struct {
	Val  int
	Next *ListNode
}

func MergeKLists(lists []*ListNode) *ListNode {
	l1 := new(ListNode)
	l1.Val = -200

	l2 := l1

	//指针
	var p *ListNode
	var index int = -1
	for {
		for i, cur := range lists {
			if cur == nil {
				continue
			}
			if index == -1 {
				p = cur
				index = i
			} else {
				if index != i {
					if p != nil && p.Val > cur.Val {
						p = cur
						index = i
					}
				}
			}
		}
		if index == -1 || p == nil {
			break
		}
		l2.Next = p
		l2 = l2.Next
		lists[index] = p.Next
		p = nil
		index = -1
	}

	return l1.Next

}
