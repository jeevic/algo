"""
207. 课程表

"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for ai, bi in prerequisites:
            graph[bi].append(ai)
        self.visited = {}
        self.onPath = {}
        self.has_cycled = False
        for i in range(numCourses):
            self.traverse(graph, i)

        return True if self.has_cycled == False else False

    visited = {}
    onPath = {}
    has_cycled = False

    def traverse(self, graph, s):
        if s in self.onPath and self.onPath[s]:
            self.has_cycled = True
        # s is traverse
        if (s in self.visited and self.visited[s]) or self.has_cycled:
            return

        self.visited[s] = True

        self.onPath[s] = True
        for neighbour in graph[s]:
            self.traverse(graph, neighbour)

        self.onPath[s] = False

        return
