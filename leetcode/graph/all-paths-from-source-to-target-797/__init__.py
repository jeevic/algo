'''
Author: caojianwei-jk caojianwei-jk@360shuke.com
Date: 2022-08-16 22:44:40
LastEditors: caojianwei-jk caojianwei-jk@360shuke.com
LastEditTime: 2025-01-01 22:15:37
FilePath: /algo/leetcode/graph/all-paths-from-source-to-target-797/__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
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
