package linklist_cycle141

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * @see  https://leetcode-cn.com/problems/linked-list-cycle/submissions/
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	p1, p2 := head, head
	for p1 != nil && p2 != nil && p1.Next != nil && p2.Next != nil && p2.Next.Next != nil {
		p1 = p1.Next
		p2 = p2.Next.Next
		if p1 == p2 {
			return true
		}
	}
	return false
}

/**
 * @see https://leetcode-cn.com/problems/linked-list-cycle-ii/
 * 检测环形链表位置
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	k := CycleLength(head)
	if k == -1 {
		return nil
	}

	//获取相距K指针移动
	return FindCycleNode(head, k)

}

func CycleLength(head *ListNode) int {
	p1, p2 := head, head.Next
	length := 0
	for p1 != nil && p2 != nil && p1.Next != nil && p2.Next != nil && p2.Next.Next != nil {
		if p1 == p2 {
			return length
		}
		p1 = p1.Next
		p2 = p2.Next.Next
		length += 1
	}
	return -1
}

func FindCycleNode(head *ListNode, k int) *ListNode {
	//k点
	p1, p2 := head, head
	for i := 0; i < k; i++ {
		p2 = p2.Next
	}

	//移动p2 p1
	for p2 != nil {
		if p1 == p2.Next {
			return p1
		}
		p1 = p1.Next
		p2 = p2.Next
	}
	return nil
}
