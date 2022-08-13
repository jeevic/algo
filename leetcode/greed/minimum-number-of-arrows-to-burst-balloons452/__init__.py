"""
452. 用最少数量的箭引爆气球
贪心算法
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        length = len(points)
        if length == 0:
            return 0

        points.sort(key=lambda x: x[1])
        right = points[0][1]
        counter = 1
        for point in points:
            left = point[0]
            if left > right:
                counter += 1
                right = point[1]

        return counter
