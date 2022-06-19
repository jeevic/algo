
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# same  1038.  https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._sum = 0
        self.traverse(root)
        return root

    _sum = 0

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.right)
        self._sum += root.val
        root.val = self._sum
        self.traverse(root.left)
