

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)

    def build(self, inorder, ins, ind, postorder, ps, pd):
        if ins > ind:
            return None

        val = postorder[pd]
        index = inorder.index(val, ins, ind + 1)

        left_size = index - ins

        root = TreeNode(val)
        root.left = self.build(inorder, ins, index - 1, postorder, ps, ps + left_size - 1)
        root.right = self.build(inorder, index + 1, ind, postorder, ps + left_size, pd - 1)
        return root
