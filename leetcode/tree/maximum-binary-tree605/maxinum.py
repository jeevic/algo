
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums)

    def construct(self, nums):
        if len(nums) == 0:
            return None

        max = nums[0]
        index = 0
        for k, v in enumerate(nums):
            if v > max:
                max = v
                index = k

        root = TreeNode(max)
        root.left = self.construct(nums[0:index])
        root.right = self.construct(nums[index+1:])
        return root

