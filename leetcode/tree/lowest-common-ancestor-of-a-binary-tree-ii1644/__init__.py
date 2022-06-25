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
