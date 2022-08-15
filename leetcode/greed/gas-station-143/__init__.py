"""
134. 加油站
"""
from typing import List


"""
暴力破解法
"""
class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            tank = 0
            for step in range(n):
                index = (i + step) % n
                tank += gas[index]
                tank -= cost[index]
                if tank <= 0:
                    break
            if tank >= 0 and step == n - 1:
                return i

        return -1


"""
sum += gas[i] - cost[i]
小于0的最低点后就开始增长  此时为开始点最合适

"""


class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        sum1 = 0
        min_sum = 0
        start = 0
        for i in range(n):
            sum1 += gas[i] - cost[i]
            if sum1 < min_sum:
                min_sum = sum1
                start = i + 1
        if sum1 < 0:
            return -1

        return start if start != n else 0

