# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            minNode = self.getMinNode(root.right)
            root.right = self.deleteNode(root.right, minNode.val)

            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMinNode(self, root):
        while root.left is not None:
            root = root.left
        return root
