# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.build(1, n)

    mem = {}

    def build(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        s = "{}-{}".format(start, end)
        r = self.mem.get(s, None)
        if r is not None:
            return r

        res = []
        i = start
        while i <= end:
            left_arr = self.build(start, i - 1)
            right_arr = self.build(i + 1, end)
            for left in left_arr:
                for right in right_arr:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
            i += 1
        self.mem[s] = res
        return res