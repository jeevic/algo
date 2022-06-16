# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.map = {}
        self.result = []
        self.traverse(root)
        return self.result

    map = {}
    result = []

    def traverse(self, root):
        if root is None:
            return None
        path = self.getChildPath(root)
        if self.map.get(path, None) is None:
            self.map[path] = 1
        else:
            self.map[path] += 1
            if self.map[path] == 2:
                self.result.append(root)

        self.traverse(root.left)
        self.traverse(root.right)

    def getChildPath(self, root):
        if root is None:
            return ""

        path = root.val
        left_val = self.getChildPath(root.left)
        right_val = self.getChildPath(root.right)
        return "{},{},{}".format(path, left_val, right_val)


class Solution2:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.map = {}
        self.result = []
        self.traverse(root)
        return self.result

    map = {}
    result = []
    def traverse(self, root):
        if root is None:
            return ""
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        path = "{},{},{}".format(left, right, root.val)
        if self.map.get(path, None) is None:
            self.map[path] = 1
        else:
            self.map[path] += 1
            if self.map[path] == 2:
                self.result.append(root)
        return path