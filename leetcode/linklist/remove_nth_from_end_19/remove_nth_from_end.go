package remove_nth_from_end_19

/**
 * 19. 删除链表的倒数第 N 个结点
 * @see https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
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
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	//特俗情况
	if head == nil {
		return head
	}

	if head.Next == nil && n == 1 {
		return nil
	}

	//查找倒插N节点位置
	p1, p2 := head, head
	for i := 1; i < n; i++ {
		p2 = p2.Next
	}
	//已经到了结尾 p1为删除节点
	if p2.Next == nil {
		head = head.Next
		p1.Next = nil
		return head
	}

	for p2 != nil && p2.Next != nil && p2.Next.Next != nil {
		p1 = p1.Next
		p2 = p2.Next
	}

	//删除
	p1.Next = p1.Next.Next

	return head
}
