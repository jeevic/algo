"""
 会议室预订

"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length <= 0:
            return 0

        begin = [0 for _ in range(length)]
        end = [0 for _ in range(length)]

        for i, interval in enumerate(intervals):
            begin[i] = interval[0]
            end[i] = interval[1]

        begin.sort()
        end.sort()

        res = 0
        i, j = 0, 0
        counter = 0

        while i < length and j < length:
            if begin[i] < end[j]:
                counter += 1
                i += 1
            else:
                counter -= 1
                j += 1
            res = max(res, counter)

        return res


"""
代码优化版本
"""


class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        ans = cur = 0
        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans
