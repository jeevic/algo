"""
990. 等式方程的可满足性
@see https://leetcode.cn/problems/satisfiability-of-equality-equations/
"""
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        a_ord = ord('a')
        uf = UnionFind(26)
        for equation in equations:
            if equation[1] == "=":
                s = equation[0]
                e = equation[3]
                uf.union(ord(s) - a_ord, ord(e) - a_ord)

        for equation in equations:
            if equation[1] == "!":
                s = equation[0]
                e = equation[3]
                if uf.connected(ord(s) - a_ord, ord(e) - a_ord):
                    return False
        return True


class UnionFind:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:
            return
        self._parent[parent_p] = self._parent[parent_q]
        self._count -= 1
        return

    def connected(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        return True if parent_q == parent_p else False

    def find(self, x):
        while self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
            x = self._parent[x]
        return self._parent[x]

    def count(self):
        return self._count
