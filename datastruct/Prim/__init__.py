"""
普罗米最小生成树算法
@see https://labuladong.github.io/algo/2/22/55/
"""
from typing import List


class Prim:
    """
    graph 是用邻接表表示的一幅图，
    graph[s] 记录节点 s 所有相邻的边，
    三元组 int[]{from, to, weight} 表示一条边
    :param graph:
     """
    def __init__(self, graph: List[List[int]]):

        n = len(graph)
        # 类似 visited 数组的作用，记录哪些节点已经成为最小生成树的一部分
        self._in_mst = [False for _ in range(n)]
        # 核心数据结构，存储「横切边」的优先级队列
        self._pq = []
        self._weight_sum = 0

        self._in_mst[0] = True
        self.cut(graph, 0)

        while len(self._pq) > 0:
            edge = self._pq.pop(0)
            to = edge[1]
            weight = edge[2]
            if self._in_mst[to]:
                continue
            self._weight_sum += weight
            self._in_mst[to] = True
            self.cut(graph, to)

    def cut(self, graph, s):
        for e in graph[s]:
            to = e[1]
            if to in self._in_mst and self._in_mst[to]:
                continue
            self._pq.append(e)

        self._pq.sort(key=lambda x: x[2])
        return

    def weight_sum(self):
        return self._weight_sum

    def all_connected(self):
        for v in self._in_mst:
            if not v:
                return False
        return True
