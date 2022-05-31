# 1011. 在 D 天内送达包裹的能力


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) <= 0:
            return 0
        left = max(weights)
        right = sum(weights) + 1

        while left < right:
            mid = left + (right - left) //2
            if self.sendWeightDays(weights, mid) == days:
                right = mid
            elif self.sendWeightDays(weights, mid) < days:
                right = mid
            elif self.sendWeightDays(weights, mid) > days:
                left = mid + 1
        return left


    def sendWeightDays(self, weights,  w):
        days = 0
        sums = 0
        for wt in weights:
            if sums + wt > w:
                sums = wt
                days += 1
            elif sums + wt == w:
                sums = 0
                days += 1
            else:
                sums += wt
        if sums > 0:
            days += 1
        return days
