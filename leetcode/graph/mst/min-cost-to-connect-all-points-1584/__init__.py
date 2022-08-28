"""
1584. 连接所有点的最小费用
@see https://leetcode.cn/problems/min-cost-to-connect-all-points/
"""

"""
最小生成树mst

"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j, abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])))

        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        cost = 0
        for ex, ey, ec in edges:
            if not uf.connected(ex, ey):
                uf.union(ex, ey)
                cost += ec

        if uf.count() == 1:
            return cost
        return 0


class UnionFind:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return
        self._parent[parent_p] = parent_q
        self._count -= 1
        return

    def connected(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return True
        return False

    def find(self, x):
        while self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
            x = self._parent[x]
        return self._parent[x]

    def count(self):
        return self._count

"""
Prim算法
"""


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                edges[i].append((i, j, abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])))
                edges[j].append((j,i, abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])))

        prim = Prim(edges)
        return prim.weight_sum()



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
