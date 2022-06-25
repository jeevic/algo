# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
遍历 + 子问题
"""
class Solution:
    deep = 0
    ancestor = None
    dp = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.deep = 0
        self.ancestor = None
        self.dp = {}
        self.getAncestor(root, p, q, 0)
        return self.ancestor

    def getAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', deep):
        if root is None:
            return
        ps = self.isChild(root, p)
        qs = self.isChild(root, q)
        if ps and qs:
            if self.ancestor is None:
                self.ancestor = root
                self.deep = deep
            else:
                if deep > self.deep:
                    self.ancestor = root
                    self.deep = deep
        if root.val == p.val or root.val == q.val:
            return
        self.getAncestor(root.left, p, q, deep + 1)
        self.getAncestor(root.right, p, q, deep + 1)

    def isChild(self, root, child):
        if root is None:
            return False
        cache_key = "{}-{}".format(root.val, child.val)
        if self.dp.get(cache_key, None) is not None:
            return self.dp.get(cache_key, None)

        if root.val == child.val:
            return True

        left = self.isChild(root.left, child)
        right = self.isChild(root.right, child)
        res = True if left == True or right == True else False
        self.dp[cache_key] = res
        return res

"""
 子问题解决思路
"""

class Solution:
    ancestor = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return False
        self.ancestor = None
        self.traverse(root, p, q)
        return self.ancestor

    def traverse(self, root, p, q):
        if root is None:
            return {}
        left = self.traverse(root.left, p, q)
        right = self.traverse(root.right, p, q)
        for k, v in right.items():
            left[k] = v
        left[root.val] = True

        if left.get(p.val, False) and left.get(q.val, False):
            if self.ancestor is None:
                self.ancestor = root
        return left