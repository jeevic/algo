"""
785. 判断二分图
"""

"""
DFS 版本
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        self.ok = True
        self.visited = {}
        self.colors = {}
        for v in range(n):
            if not self.visited.get(v, False):
                self.colors[v] = False
                self.traverse(graph, v)
        return self.ok

    ok = True
    visited = {}
    colors = {}

    def traverse(self, graph, v):
        if not self.ok:
            return
        self.visited[v] = True
        for g in graph[v]:
            if not self.visited.get(g, False):
                self.colors[g] = not self.colors[v]
                self.traverse(graph, g)
            else:
                if self.colors[v] == self.colors[g]:
                    self.ok = False
                    return


"""
BFS 版本
"""


class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.ok = True
        self.visited = {}
        self.colors = {}
        queue = []
        for i in range(n):
            if not self.visited.get(i, False):
                self.colors[i] = False
                self.bfs(graph, i)
        return self.ok

    ok = True
    visited = {}
    colors = {}

    def bfs(self, graph, v):
        queue = [v]

        while len(queue) > 0 and self.ok:
            v = queue.pop(0)
            self.visited[v] = True
            for neighbor in graph[v]:
                if not self.visited.get(neighbor, False):
                    self.colors[neighbor] = not self.colors[v]
                    queue.append(neighbor)
                else:
                    if self.colors[neighbor] == self.colors[v]:
                        self.ok = False
                        return
