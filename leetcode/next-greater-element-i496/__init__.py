
"""
暴力法
时间复杂度:o(n^2)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [ - 1 for i in range(len(nums1))]
        length2 = len(nums2)
        for k,v in enumerate(nums1):
            index = nums2.index(v)
            i = index + 1
            while i < length2:
                if nums2[index] < nums2[i]:
                    res[k] =  nums2[i]
                    break
                i += 1
        return res



"""
倒取 单调栈
复杂度:o(n)
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res_map = self.nextGreaterNums(nums2)
        res = [-1 for i in range(len(nums1))]
        for k, v in enumerate(nums1):
            res[k] = res_map[v]
        return res

    def nextGreaterNums(self, nums2):
        length = len(nums2)
        i = length - 1
        stack = []
        res = {}
        while i >= 0:
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            res[nums2[i]] = stack[-1] if len(stack) >0 else -1
            stack.append(nums2[i])
            i -= 1
        return res