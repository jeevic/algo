"""
435. 无重叠区间
 贪心算法
 @see https://leetcode.cn/problems/non-overlapping-intervals/
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length <= 0:
            return 0
        intervals.sort(key=lambda r: r[1])
        end = intervals[0][1]
        counter = 1
        for interval in intervals:
            if interval[1] > end:
                counter += 1
                end = interval[1]

        return length - counter

