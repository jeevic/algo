"""
130. 被围绕的区域
"""


"""
DFS算法
遍历所有边框如果是O, 使用dfs将相邻节点替换#
遍历所有区域将O 替换成 X 将#替换成 O
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = "X"
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        return

    def dfs(self, board, i, j):
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return

        if board[i][j] == "O":
            board[i][j] = "#"
        else:
            return
        dt = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for x, y in dt:
            self.dfs(board, i + x, j + y)
        return


"""
并查集  unionfind
将边界所有O 映射到 dummy 上
将所有相连O联通
遍历所有O不和 dummy 联通置为 X
"""


class Solution3:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        uf = UnionFind(m * n + 1)
        dummy = m * n

        for i in range(m):
            if board[i][0] == "O":
                uf.union(i * n, dummy)
            if board[i][n - 1] == "O":
                uf.union(i * n + n - 1, dummy)

        for j in range(n):
            if board[0][j] == "O":
                uf.union(j, dummy)
            if board[m - 1][j] == "O":
                uf.union((m - 1) * n + j, dummy)

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    for x, y in d:
                        if 0 <= i + x < m and 0 <= j + y < n:
                            if board[i + x][j + y] == "O":
                                uf.union(i * n + j, (i + x) * n + j + y)

        for i in range(m):
            for j in range(n):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = "X"

        return board


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
