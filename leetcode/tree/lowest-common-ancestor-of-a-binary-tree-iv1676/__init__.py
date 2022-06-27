class Solution:
    ancestor = None

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.traverse(root, nodes)
        return self.ancestor

    def traverse(self, root, nodes):
        if root is None:
            return {}

        left = self.traverse(root.left, nodes)
        right = self.traverse(root.right, nodes)

        for k, v in right.items():
            left[k] = v
        left[root.val] = True

        is_all = True
        for node in nodes:
            if left.get(node.val, False) is False:
                is_all = False
                break
        if is_all:
            if self.ancestor is None:
                self.ancestor = root

        return left

"""
遍历 子问题
"""

class Solution1:

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes_map = {}
        for node in nodes:
            nodes_map[node.val] = True
        return self.find(root, nodes_map)

    def find(self, root, np):
        if root is None:
            return None

        if np.get(root.val, False):
            return root

        left = self.find(root.left, np)
        right = self.find(root.right, np)

        if left is not None and right is not None:
            return root
        return left if left is not None else right
