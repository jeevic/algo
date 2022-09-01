"""
51. N 皇后
https://leetcode.cn/problems/n-queens/
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = ["." * n for _ in range(n)]
        self.backtrace(board, 0)
        return self.res

    res = []

    def backtrace(self, board, row):
        if row == len(board):
            self.res.append(board.copy())
            return

        n = len(board[row])
        for i in range(n):
            if not self.is_valid(board, row, i):
                continue
            rs = board[row]
            rl = list(rs)
            rl[i] = "Q"
            board[row] = "".join(rl)
            self.backtrace(board, row + 1)
            rl[i] = "."
            board[row] = "".join(rl)
        return True

    def is_valid(self, board, row, col):
        for r in range(row):
            if board[r][col] == "Q":
                return False
        n = len(board[row])
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        return True
