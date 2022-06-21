# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        self.mid_sorted = []
        self.traverse(root)
        return self.result

    mid_sorted = []
    result = True

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if len(self.mid_sorted) > 0:
            if self.mid_sorted[-1] >= root.val:
                self.result = False
                return
        self.mid_sorted.append(root.val)
        self.traverse(root.right)


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root, None, None)

    def validBST(self, root, min, max):
        if root is None:
            return True

        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False

        left = self.validBST(root.left, min, root.val)
        right = self.validBST(root.right, root.val, max)

        return left and right
