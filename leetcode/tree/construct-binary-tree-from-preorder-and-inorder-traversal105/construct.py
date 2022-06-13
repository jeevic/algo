class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


    def build(self, preorder, ps, pd, inorder, it, id) -> TreeNode:
        if ps > pd:
            return None

        val = preorder[ps]
        index = inorder.index(val, it, id + 1)
        left_size = index - it

        root = TreeNode(val)
        root.left = self.build(preorder, ps+1, ps+left_size, inorder, it, index - 1)
        root.right = self.build(preorder, ps+left_size + 1, pd, inorder, index + 1, id)
        return root

