"""
相同题:
 239: https://leetcode.cn/problems/sliding-window-maximum/
 剑指 Offer 59 : https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
 剑指 Offer 59 - II:  https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        i = 0
        q = MQ()
        res = []
        while i < length:
            if i < k - 1:
                q.insert(nums[i])
            else:
                q.insert(nums[i])
                res.append(q.max())
                if q.peek() == nums[i - k + 1]:
                    q.pop()
            i += 1
        return res


class MQ:
    def __init__(self):
        self.q = []

    def insert(self, e):
        while len(self.q) > 0 and self.q[-1] < e:
            self.q.pop()
        self.q.append(e)

    def pop(self):
        return self.q.pop(0)

    def peek(self):
        return self.q[0] if len(self.q) > 0 else None

    def max(self):
        return self.peek()

    def size(self):
        return len(self.q)
