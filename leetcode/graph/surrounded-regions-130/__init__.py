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
