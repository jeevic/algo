"""
797. 所有可能的路径
"""
from typing import List


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        path = []
        self.traverse(graph, 0, path)
        return self.result

    result = []

    def traverse(self, graph, cur, path):
        path.append(cur)
        length = len(graph)

        if cur == length - 1:
            self.result.append(path.copy())
            path.pop()
            return

        for neighbour in graph[cur]:
            self.traverse(graph, neighbour, path)

        path.pop()
