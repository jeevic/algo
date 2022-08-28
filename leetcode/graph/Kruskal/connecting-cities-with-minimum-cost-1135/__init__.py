"""
1135. 最低成本联通所有城市
@see https://leetcode.cn/problems/connecting-cities-with-minimum-cost/
"""

"""
最小生成树mst
Kruskal 算法
"""


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        uf = UnionFind(n + 1)
        cost = 0
        for s, e, c in connections:
            if not uf.connected(s, e):
                uf.union(s, e)
                cost += c

        if uf.count() == 2:
            return cost
        return -1


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
