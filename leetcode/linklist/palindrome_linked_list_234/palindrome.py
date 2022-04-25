# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return False

        listNode = []
        while head != None:
            listNode.append(head)
            head = head.next

        j, k = len(listNode) // 2, len(listNode) // 2
        if len(listNode) % 2 == 0:
            j = len(listNode) // 2 - 1
            k = len(listNode) // 2
        else:
            j = len(listNode) // 2
            k = len(listNode) // 2

        while j >= 0 and k <= len(listNode) - 1:
            if listNode[j].val != listNode[k].val:
                return False
            j = j - 1
            k = k + 1
        return True


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return False
        self.first_node = head
        return self.recursion(head)

    first_node = None
    def recursion(self, head:  ListNode):
        if head == None:
            return True
        r = self.recursion(head.next)
        r = r and (self.first_node.val == head.val)
        self.first_node = self.first_node.next
        return r


class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return False
        # 找中点
        fast = slow = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        if fast.next != None:
            slow = slow.next
        last = self.reverse(slow)

        p1 = head
        p2 = last
        while p1 != None and p2 != None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        self.reverse(last)
        return True

    def reverse(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last