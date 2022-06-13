# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = self.traver(root, 1)
        return depth

    def traver(self, root: Optional[TreeNode], depth: int):
        if root is None:
            return depth - 1

        depth = max(self.traver(root.left, depth + 1),  self.traver(root.right, depth + 1))
        return depth




class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1



class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res

    depth = 0
    res = 0

    def traverse(self, root):
        if root is None:
            return
        self.depth += 1

        self.res = max(self.res, self.depth)

        self.traverse(root.left)
        self.traverse(root.right)

        self.depth -= 1
