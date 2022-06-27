"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_map = {}
        cur = p
        while cur is not None:
            p_map[cur.val] = True
            cur = cur.parent

        cur = q
        while cur is not None:
            if p_map.get(cur.val, False):
                return cur
            cur = cur.parent
        return None


"""
链表相交思路
"""


class Solution:

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        i = p
        j = q
        while i.val != j.val:
            i = i.parent
            j = j.parent

            if i is None:
                i = q
            if j is None:
                j = p

        return i
