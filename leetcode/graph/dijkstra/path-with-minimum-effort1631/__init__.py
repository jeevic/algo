"""
1631. 最小体力消耗路径
@see https://leetcode.cn/problems/path-with-minimum-effort/
"""
from typing import List

"""
dijkstra最短路基算法原理
"""


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = []
        m = len(heights)
        n = len(heights[0])
        if m == 1 and n == 1:
            return 0
        dis_to = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        dis_to[0][0] = 0
        queue = [(0, 0, 0)]

        while len(queue) > 0:
            cur_x, cur_y, c_h = queue.pop(0)
            height = heights[cur_x][cur_y]

            if cur_x == m - 1 and cur_y == n - 1:
                return c_h

            if dis_to[cur_x][cur_y] < c_h:
                continue

            for neighbour in self.get_neighbour(cur_x, cur_y, m, n):
                nx, ny = neighbour[0], neighbour[1]
                n_height = heights[nx][ny]
                n_h = abs(n_height - height)
                n_h = n_h if c_h < n_h else c_h

                if dis_to[nx][ny] > n_h:
                    dis_to[nx][ny] = n_h
                    queue.append((nx, ny, n_h))

            queue.sort(key=lambda x: x[2])
        return dis_to[m - 1][n - 1]

    def get_neighbour(self, x, y, m, n):
        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        neighbours = []
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            else:
                neighbours.append([nx, ny])
        return neighbours


"""
二分法 + bfs
时间复杂度: O(mnlog(C)) C为最大10**6 及height高度

"""


class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ### 二分查找height + bfs
        left = 0
        right = 10 ** 6 - 1
        m = len(heights)
        n = len(heights[0])
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            seen = [(0, 0)]

            queue = [(0, 0)]
            while len(queue) > 0:
                cx, cy = queue.pop(0)
                for nx, ny in [(cx - 1, cy), (cx, cy - 1), (cx + 1, cy), (cx, cy + 1)]:
                    if 0 <= nx < m and 0 <= ny < n and abs(heights[nx][ny] - heights[cx][cy]) <= mid and (
                    nx, ny) not in seen:
                        queue.append((nx, ny))
                        seen.append((nx, ny))

            if (m - 1, n - 1) in seen:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

"""
unionfind 
并查集方法
计算所有下 和 右侧 元素差值
进行升序排序 然后并集集计算(0,0)到（m-1， n-1)连通性
"""


class Solution3:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        diff_heights = [(0, 0, 0)]

        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                ds = [(i + 1, j), [i, j + 1]]
                for dx, dy in ds:
                    if 0 <= dx < m and 0 <= dy < n:
                        diff_heights.append((i * n + j, dx * n + dy, abs(heights[dx][dy] - heights[i][j])))
        diff_heights.sort(key=lambda x: x[2])

        ans = 0
        for x, y, dh in diff_heights:
            uf.union(x, y)
            if uf.connectd(0, m * n - 1):
                ans = dh
                break

        return ans


class UnionFind:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]

    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return True
        self._parent[parent_p] = parent_q
        self._count -= 1
        return

    def connectd(self, p, q):
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