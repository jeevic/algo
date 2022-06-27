# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ancestor = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return False
        self.ancestor = None
        self.traverse(root, p, q)
        return self.ancestor

    def traverse(self, root, p, q):
        if root is None:
            return {}
        left = self.traverse(root.left, p, q)
        right = self.traverse(root.right, p, q)
        for k, v in right.items():
            left[k] = v
        left[root.val] = True

        if left.get(p.val, False) and left.get(q.val, False):
            if self.ancestor is None:
                self.ancestor = root
        return left


class Solution2:
    fp = False
    fq = False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.fp = False
        self.fq = False
        res = self.find(root, p.val, q.val)
        if res is not None:
            if self.fp and self.fq:
                return res
        return None

    def find(self, root, val1, val2):
        if root is None:
            return None

        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)

        if left is not None and right is not None:
            return root

        if root.val == val1 or root.val == val2:
            if root.val == val1:
                self.fp = True
            if root.val == val2:
                self.fq = True
            return root
        return left if right is None else right

