"""
743. 网络延迟时间
@see https://leetcode.cn/problems/network-delay-time/
"""
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 图
        graph = self.build_graph(n, times)

        # 距离
        dst_to = [sys.maxsize for _ in range(n + 1)]
        dst_to[k] = 0
        max1 = 0

        queue = [(k, 0)]

        while len(queue) > 0:
            cur_id, cur_w = queue.pop(0)
            if cur_w > dst_to[cur_id]:
                continue
            for neighbor_id, neighbor_w in graph[cur_id]:
                dst = cur_w + neighbor_w
                if dst_to[neighbor_id] > dst:
                    dst_to[neighbor_id] = dst
                    queue.append([neighbor_id, dst])

            queue.sort(key=lambda x: x[1])

        for i in range(1, n + 1):
            if dst_to[i] == sys.maxsize:
                return -1
        return max(dst_to[1:])

    def build_graph(self, n, times):
        graph = [[] for _ in range(n + 1)]
        for time in times:
            graph[time[0]].append([time[1], time[2]])

        return graph
