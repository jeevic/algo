package middle_link_list_876

/**
 * 链表的中间点
 * @see https://leetcode-cn.com/problems/middle-of-the-linked-list/  876. 链表的中间结点
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
func middleNode(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	p1, p2 := head, head
	for p2 != nil && p2.Next != nil && p2.Next.Next != nil {
		p1 = p1.Next
		p2 = p2.Next.Next
	}
	if p2 != nil && p2.Next != nil {
		p1 = p1.Next
	}
	return p1
}
