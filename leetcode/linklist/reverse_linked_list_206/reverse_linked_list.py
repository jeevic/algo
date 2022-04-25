# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        # a -> b  b -> a
        pre = None
        while head != None:
            # b
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre



class Solution2:

    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        # a -> b  b -> a
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


    def reverseListN(self, head: ListNode, n :int):
        if head == None or head.next == None:
            return head
        pre = None
        i = 0
        first = head
        while i < n and head is not None:
            i += 1
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        first.next = head

        return pre

    def reverseListN2(self, head: ListNode, n: int):
        if head == None or head.next == None or n <= 0:
            return head
        last, ln = self.reverseListRecursion(head, n)
        head.next = ln
        return last

    def reverseListRecursion(self, head: ListNode, n: int):
        if head == None or head.next == None:
            return (head, None)
        if n <= 1 :
            return head, head.next
        last,ln = self.reverseListN2(head.next, n - 1)
        head.next.next = head
        head.next = None
        return last, ln


    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None or head.next == None:
            return head

        l_node = None
        l_node_pre = None
        r_node = None
        r_node_after = None
        pre = None
        temp = head
        l = 0
        while temp != None and l <= right:
            l += 1
            if l == left:
                l_node_pre = pre
                l_node = temp
            if l == right:
                r_node = temp
                r_node_after = temp.next
            if l > left and l <= right:
                cur = temp
                temp = temp.next
                cur.next = pre
                pre = cur
            else:
                pre = temp
                temp = temp.next
                if l == left:
                    pre.next = None
        if l_node_pre == None:
            head.next = r_node_after
            head = r_node
        elif r_node_after == None:
            l_node_pre.next = r_node
            l_node.next = None
        else:
            l_node_pre.next = r_node
            l_node.next = r_node_after

        return head


class Solution3:
    ender = None
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """反转前N个节点"""
        if left == 1:
            self.ender = None
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            self.ender = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = ender
        return last



class Solution4:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        first = True
        pre = head
        while cur != None:
            self.ender = None
            self.reverse = True
            last, follow = self.reverseN(cur, k)

            if last is None:
                break
            if first is True and last is not None:
                head = last
                first = False
            else:
                pre.next = last
            pre = cur
            cur = follow
        return head

    ender = None
    reverse = True
    def reverseN(self, head: Optional[ListNode], k: int):
        if k == 1:
           self.ender = head.next
           return head, self.ender
        if head.next is None:
            self.ender = None
            self.reverse = False
            return None, None
        last, follow  = self.reverseN(head.next, k - 1)
        if self.reverse is True:
            head.next.next = head
            head.next = self.ender
        return last, follow








