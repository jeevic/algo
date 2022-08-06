"""
打家劫舍-3
"""
from typing import Optional


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.mem = {}
        return self.dp(root)

    mem = {}

    def dp(self, root):
        if root is None:
            return 0
        if root in self.mem:
            return self.mem[root]
        # 抢当前
        cur_rob = root.val
        if root.left is not None:
            cur_rob += (self.dp(root.left.left) + self.dp(root.left.right))
        if root.right is not None:
            cur_rob += (self.dp(root.right.left) + self.dp(root.right.right))

            # 不抢当前
        cur_unrob = self.dp(root.left) + self.dp(root.right)
        res = max(cur_rob, cur_unrob)
        self.mem[root] = res
        return res


class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dp(root))

    def dp(self, root):
        if root is None:
            return (0, 0)

        left = self.dp(root.left)
        right = self.dp(root.right)

        # 抢当前
        rob = root.val + left[0] + right[0]
        # 不抢当前
        unrob = max(left) + max(right)
        return (unrob, rob)
