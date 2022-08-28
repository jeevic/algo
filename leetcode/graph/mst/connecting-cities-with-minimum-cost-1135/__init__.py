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

"""
Prim 算法
"""


class Solution2:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph = self.build_graph(n, connections)
        prim = Prim(graph)
        if not prim.all_connected():
            return -1
        return prim.weight_sum()

    def build_graph(self, n, connections):
        graph = [[] for _ in range(n)]
        for connection in connections:
            graph[connection[0] - 1].append((connection[0] - 1, connection[1] - 1, connection[2]))
            graph[connection[1] - 1].append((connection[1] - 1, connection[0] - 1, connection[2]))
        return graph


class Prim:
    def __init__(self, graph):
        n = len(graph)
        self._pq = []
        self._in_mst = [False for _ in range(n)]
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
        for edge in graph[s]:
            to = edge[1]
            if self._in_mst[to]:
                continue
            self._pq.append(edge)
        self._pq.sort(key=lambda x: x[2])

    def weight_sum(self):
        return self._weight_sum

    def all_connected(self):
        for v in self._in_mst:
            if not v:
                return False
        return True