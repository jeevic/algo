

# @see https://leetcode.cn/problems/binary-tree-preorder-traversal/

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        self.preTraversal(root, ls)
        return ls

    def preTraversal(self, root: Optional[TreeNode], ls: List[int]):
        if root is None:
            return
        ls.append(root.val)
        self.preTraversal(root.left, ls)
        self.preTraversal(root.right, ls)


