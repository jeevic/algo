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
