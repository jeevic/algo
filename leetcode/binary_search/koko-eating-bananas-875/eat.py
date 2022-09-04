from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1

        left = 1
        right = 1000000001

        while left < right:
            mid = left + (right - left) // 2
            if self.eatHours(piles, mid) == h:
                right = mid
            elif self.eatHours(piles, mid) < h:
                right = mid
            elif self.eatHours(piles, mid) > h:
                left = mid + 1
        return left

        # eat hours

    def eatHours(self, piles, k):
        h = 0
        for item in piles:
            h += int(item / k)
            if item % k > 0:
                h += 1
        return h
