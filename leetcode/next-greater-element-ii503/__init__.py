
"""
单调栈
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums1 = nums + nums
        length = len(nums1)
        res = [-1 for i in range(length)]

        stack = []
        i = length - 1
        while i >= 0:
            while len(stack) > 0 and stack[-1] <= nums1[i]:
                stack.pop()
            res[i] = stack[-1] if len(stack) > 0 else -1
            stack.append(nums1[i])
            i -= 1
        return res[0:len(nums)]
