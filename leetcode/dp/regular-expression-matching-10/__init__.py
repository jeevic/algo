"""
 正则表达式
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.mem = {}
        return self.dp(s, 0, p, 0)

    mem = {}

    def dp(self, s, i, p, j):
        # base case
        if len(s) == i and len(p) == j:
            return True
        if len(s) == i:
            while j + 1 < len(p) and p[j + 1] == "*":
                j += 2
            if j == len(p):
                return True
            return False
        if i < len(s) and len(p) == j:
            return False

        if (i, j) in self.mem:
            return self.mem[(i, j)]

        if s[i] == p[j] or p[j] == ".":
            if j < len(p) - 1 and p[ j +1] == "*":
                res = self.dp(s, i + 1, p, j) or  self.dp(s, i, p, j+ 2)
            else:
                res = self.dp(s, i + 1, p, j + 1)
        else:
            # 不相等 只能忽略当前了
            if j < len(p) - 1 and p[j + 1] == "*":
                res = self.dp(s, i, p, j + 2)
            else:
                res = False
        self.mem[(i, j)] = res
        return res