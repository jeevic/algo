"""
261. 以图判树
@see https://leetcode.cn/problems/graph-valid-tree/
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for ea, eb in edges:
            if uf.connected(ea, eb):
                return False
            uf.union(ea, eb)
        return True if uf.count() == 1 else False


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
