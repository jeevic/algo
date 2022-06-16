class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, preorder, ps, pd, postorder, ts, td):
        if td - ts == 0:
            return TreeNode(postorder[ts])
        if ps > pd:
            return None
        if ts > td:
            return None

        val = preorder[ps]

        leftval = preorder[ps + 1]
        index = postorder.index(leftval)

        left_size = index - ts + 1

        root = TreeNode(val)
        root.left = self.build(preorder, ps + 1, ps + left_size, postorder, ts, index)
        root.right = self.build(preorder, ps + left_size + 1, pd, postorder, index + 1, td - 1)
        return root
