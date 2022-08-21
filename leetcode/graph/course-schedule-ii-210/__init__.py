"""
210. 课程表 II

@see https://leetcode.cn/problems/course-schedule-ii/
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        length = len(prerequisites)
        graph = [[] for _ in range(numCourses)]

        for requeisite in prerequisites:
            graph[requeisite[1]].append(requeisite[0])

        self.result = []
        self.has_cycled = False
        self.visited = {}
        self.visited = {}
        for fr, to in enumerate(graph):
            self.traverse(graph, fr)
        if self.has_cycled:
            return []
        self.result.reverse()
        return self.result

    result = []
    has_cycled = False
    visited = {}
    v_path = {}

    def traverse(self, graph, cur):

        if cur in self.v_path and self.v_path[cur]:
            self.has_cycled = True

        if (cur in self.visited and self.visited[cur]) or self.has_cycled:
            return

        self.visited[cur] = True
        self.v_path[cur] = True

        for neighbor in graph[cur]:
            self.traverse(graph, neighbor)

        self.v_path[cur] = False
        self.result.append(cur)


"""
BFS 
"""


class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        for requisite in prerequisites:
            graph[requisite[1]].append(requisite[0])
            indegree[requisite[0]] += 1

        result = []
        queue = []
        count = 0
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while len(queue) > 0:
            cur = queue.pop(0)
            count += 1
            result.append(cur)
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)

        if count == numCourses:
            return result
        return []
