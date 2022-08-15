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
