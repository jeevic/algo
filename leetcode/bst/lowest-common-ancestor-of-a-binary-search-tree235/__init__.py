# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        left = p
        right = q
        if p.val > q.val:
            right = p
            left = q
        if root.val > left.val and root.val < right.val:
            return root
        elif root.val == left.val or root.val == right.val:
            return root
        elif root.val > left.val and root.val > right.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < left.val and root.val < right.val:
            return self.lowestCommonAncestor(root.right, p, q)



