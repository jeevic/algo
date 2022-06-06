# create-maximum-number


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        counter = k if nums1_len >= k else nums1_len

        result = []
        i = 0
        while i <= counter:
            if nums2_len - k + i < 0:
                i += 1
                continue
            l = self.merge_list(self.pick_max(nums1, i), self.pick_max(nums2, k - i))
            if l > result:
                result = l
            i += 1
        return result


    def pick_max(self, nums:List[int], k: int) -> List[int]:
        drop_n = len(nums) - k
        stack = []

        for v in nums:
            while drop_n > 0 and len(stack) > 0 and stack[-1] < v:
                stack.pop()
                drop_n -= 1
            stack.append(v)
        return stack[:k]


    def merge_list(self, pick1:List[int], pick2: List[int]) -> List[int]:
        new_list = []
        while len(pick1) > 0 and len(pick2) > 0:
            temp = pick1 if pick1 > pick2  else pick2
            new_list.append(temp.pop(0))
        if len(pick1) > 0:
            new_list.extend(pick1)

        if len(pick2) > 0:
            new_list.extend(pick2)

        return new_list

