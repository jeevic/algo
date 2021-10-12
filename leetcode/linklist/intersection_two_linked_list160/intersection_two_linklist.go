package intersection_two_linked_list160

/**
 * 160 相交链表相交点
 * @see https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
 * @see https://labuladong.gitee.io/algo/1/6/
 * @see https://github.com/labuladong/fucking-algorithm
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}

	p1, p1Tail := headA, headA
	for p1Tail.Next != nil {
		p1Tail = p1Tail.Next
	}

	p1Tail.Next = p1

	k := CycleLength(headB)
	if k == -1 {
		p1Tail.Next = nil
		return nil
	}

	p3 := FindCycleNode(headB, k)
	p1Tail.Next = nil
	return p3
}

func getIntersectionNode2(headA, headB *ListNode) *ListNode {
	p1, p2 := headA, headB
	p1Sign, p2Sign := false, false
	for p1 != p2 {
		if p1 == nil {
			if p1Sign == false {
				p1Sign = true
				p1 = headB
			} else {
				break
			}
		} else {
			p1 = p1.Next
		}
		if p2 == nil {
			if p2Sign == false {
				p2Sign = true
				p2 = headA
			} else {
				break
			}
		} else {
			p2 = p2.Next
		}
	}
	if p1 == p2 && p1 != nil {
		return p1
	}

	return nil
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
