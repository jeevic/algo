
"""
遍历法 O(N)
"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        hi = 0
        hr = 0
        l = root
        while l is not None:
            l = l.left
            hi += 1

        while l is not None:
            l = l.right
            hr += 1
        if hi == hr:
            return int(math.pow(2, hi)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
