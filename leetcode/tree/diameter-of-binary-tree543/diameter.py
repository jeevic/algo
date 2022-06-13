
# @see https://leetcode.cn/problems/diameter-of-binary-tree/


class Solution:
    max_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterSubTree(root)
        return self.max_length - 1 if self.max_length > 1 else 0


    def diameterSubTree(self, root):
        if root is None:
            return 0

        left = self.diameterSubTree(root.left)

        right = self.diameterSubTree(root.right)

        if self.max_length < left + right + 1:
            self.max_length = left + right + 1

        return max(left + 1, right + 1)

