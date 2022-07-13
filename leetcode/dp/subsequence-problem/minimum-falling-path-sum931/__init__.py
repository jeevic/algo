
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l1 = len(matrix)
        l2 = len(matrix[0])
        dp = [[sys.maxsize for i in range(l2)] for i in range(l1)]

        for i in range(l2):
            dp[0][i] = matrix[0][i]

        i = 1
        while i < l1:
            j = 0
            while j < l2:
                dp[i][j] = min(self.get_martix_e(dp, i - 1, j - 1), self.get_martix_e(dp, i - 1, j),
                               self.get_martix_e(dp, i - 1, j + 1)) + matrix[i][j]
                j += 1
            i += 1
        res = min(dp[l1 - 1])
        return res

    def get_martix_e(self, dp, i, j):
        l1 = len(dp)
        l2 = len(dp[0])
        if i < 0 or i >= l1:
            return sys.maxsize
        if j < 0 or j >= l2:
            return sys.maxsize
        return dp[i][j]

