"""
886. 可能的二分法
@see https://leetcode.cn/problems/possible-bipartition/
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.build_graph(dislikes, n)
        self.ok = True
        self.visited = {}
        self.colors = {}
        for i in range(1, n + 1):
            if not self.visited.get(i, False):
                self.colors[i] = False
                self.traverse(graph, i)

        return self.ok

    ok = True
    visited = {}
    colors = {}

    def build_graph(self, dislikes, n):
        graph = [[] for _ in range(n + 1)]
        for fr, to in enumerate(dislikes):
            graph[to[1]].append(to[0])
            graph[to[0]].append(to[1])
        return graph

    def traverse(self, graph, v):
        if not self.ok:
            return
        self.visited[v] = True
        for g in graph[v]:
            if not self.visited.get(g, False):
                self.colors[g] = not self.colors[v]
                self.traverse(graph, g)
            else:
                if self.colors[g] == self.colors[v]:
                    self.ok = False
                    return


"""
BFS 版本
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.build_graph(dislikes, n)
        self.ok = True
        self.visited = {}
        self.colors = {}
        for i in range(1, n + 1):
            if not self.visited.get(i, False):
                self.colors[i] = False
                self.bfs(graph, i)

        return self.ok

    ok = True
    visited = {}
    colors = {}

    def build_graph(self, dislikes, n):
        graph = [[] for _ in range(n + 1)]
        for fr, to in enumerate(dislikes):
            graph[to[1]].append(to[0])
            graph[to[0]].append(to[1])
        return graph

    def bfs(self, graph, v):
        queue = [v]
        self.visited[v] = True
        while len(queue) > 0 and self.ok:
            v = queue.pop(0)
            for neighbor in graph[v]:
                if not self.visited.get(neighbor, False):
                    self.colors[neighbor] = not self.colors[v]
                    self.visited[neighbor] = True
                    queue.append(neighbor)
                else:
                    if self.colors[v] == self.colors[neighbor]:
                        self.ok = False
                        return
