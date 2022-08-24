"""
323. 无向图中连通分量的数目
@see https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/
"""

"""
DFS遍历 + visited
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.visited = {}
        count = 0
        for i in range(n):
            if not self.visited.get(i, False):
                self.dfs(graph, i)
                count += 1
        return count

    visited = {}

    def dfs(self, graph, v):
        if self.visited.get(v, False):
            return
        self.visited[v] = True
        for neighbor in graph[v]:
            self.dfs(graph, neighbor)
        return



"""
BFS 版本
"""


class Solution1:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.visited = {}
        count = 0
        for i in range(n):
            if not self.visited.get(i, False):
                self.bfs(graph, i)
                count += 1
        return count

    visited = {}

    def bfs(self, graph, v):
        queue = []
        self.visited[v] = True
        queue.append(v)

        while len(queue) > 0:
            v = queue.pop(0)
            for neighbor in graph[v]:
                if not self.visited.get(neighbor, False):
                    self.visited[neighbor] = True
                    queue.append(neighbor)

        return


"""
union find 
并查集写法
"""


class Solution3:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        return uf.count()


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
