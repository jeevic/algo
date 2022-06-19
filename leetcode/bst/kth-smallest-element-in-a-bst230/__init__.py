# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        self.sorted = []
        self.traverse(root)
        return self.sorted[k-1]
    sorted = []
    def  traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.sorted.append(root.val)
        self.traverse(root.right)
