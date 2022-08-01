"""
787. K 站中转内最便宜的航班
"""
import sys
from typing import List

"""
思路一 动态规划
自顶而下
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if len(flights) <= 0:
            return -1
        dst_flights = {}
        self.mem = {}
        for flight in flights:
            fr, to, price = flight[0], flight[1], flight[2]
            if to in dst_flights:
                dst_flights[to].append([fr, price])
            else:
                dst_flights[to] = [[fr, price]]
        return self.dp(dst_flights, src, dst, k)

    mem = {}

    def dp(self, dst_flights, src, dst, k):
        key = (src, dst, k)
        if key in self.mem:
            return self.mem[key]
        froms = dst_flights.get(dst, [])

        # base
        if src == dst:
            return 0
        if k == 0:
            for item in froms:
                if item[0] == src:
                    return item[1]
            return -1
        res = sys.maxsize
        for item in froms:
            r = self.dp(dst_flights, src, item[0], k - 1)
            if r == -1:
                continue
            res = min(res, r + item[1])
        if res == sys.maxsize:
            res = -1
        self.mem[key] = res
        return res


"""
 思路二:  Dijkstra  最短路径
"""


class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if len(flights) <= 0:
            return -1
        graph = {}
        for flight in flights:
            fr, to, price = flight
            if fr in graph:
                graph[fr].append([to, price])
            else:
                graph[fr] = [[to, price]]

        return self.dijstra(graph, src, dst, k + 1)

    def dijstra(self, graph, src, dst, k):
        # 定义：从起点 src 到达节点 i 的最短路径权重为 distTo[i]
        dst_to = [sys.maxsize for _ in range(len(graph) + 1)]
        # 定义：从起点 src 到达节点 i 至少要经过 nodeNumTo[i] 个节点
        node_num_to = [sys.maxsize for i in range(len(graph) + 1)]

        dst_to[src] = 0
        node_num_to[src] = 0

        queue = []
        queue.append(State(src, 0, 0))

        while len(queue) > 0:
            st = queue.pop(0)
            cur_id = st.id
            cur_cost = st.cost_from_src
            cur_node_nums = st.node_num_from_src

            if cur_id == dst:
                return cur_cost

            if cur_node_nums == k:
                continue

            for neighbor in graph[cur_id]:
                next_id = neighbor[0]
                next_cost = cur_cost + neighbor[1]
                next_node_nums = cur_node_nums + 1

                if dst_to[next_id] > next_cost:
                    dst_to[next_id] = next_cost
                    node_num_to[next_id] = next_node_nums

                # 剪枝，如果中转次数更多，花费还更大，那必然不会是最短路径
                if next_cost > dst_to[next_id] and next_node_nums > node_num_to[next_id]:
                    continue
                queue.append(State(next_id, next_cost, next_node_nums))

        return -1


class State:
    def __init__(self, id, cost_from_src, node_num_from_src):
        self.id = id
        self.cost_from_src = cost_from_src
        self.node_num_from_src = node_num_from_src

