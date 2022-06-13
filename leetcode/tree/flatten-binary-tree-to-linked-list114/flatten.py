class Solution:
    def flatten(self, root: TreeNode) -> None:

        """
        Do not return anything, modify root in-place instead.
        """

        self.p = self.dummy
        self.traverse(root)
        print(self.dummy.right)
        return self.dummy.right

    dummy = TreeNode(-1)
    p = None
    def traverse(self, root):
        if root == None:
            return
        self.p.right = TreeNode(root.val)
        self.p.left = None
        self.p = self.p.right

        self.traverse(root.left)
        self.traverse(root.right)


class Solution2:
    def flatten(self, root: TreeNode) -> None:

        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)

        return root

    def traverse(self, root):
        if root is None:
            return None

        self.traverse(root.left)
        self.traverse(root.right)

        temp = root.right
        root.right = root.left
        root.left = None

        p = root
        while p.right is not None:
            p = p.right
        p.right = temp


class Solution3:
    def flatten(self, root: TreeNode) -> None:

        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)

        return root

    def traverse(self, root):
        if root is None:
            return None
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        root.right = left
        root.left = None

        p = root.right
        while p is not None and p.right is not None:
            p = p.right
        if p is not None:
            p.right = right
        elif right is not None:
            root.right = right
        return root
