
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)


class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.traverse(root)

    def traverse(self, root):
        if root is None:
            return root
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        root.left, root.right = right, left
        return root

