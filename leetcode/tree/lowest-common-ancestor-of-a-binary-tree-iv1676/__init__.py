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
