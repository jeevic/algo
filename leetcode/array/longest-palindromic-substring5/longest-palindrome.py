class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 0:
            return ""
        p = 0
        q = len(s) -1

        res = s[0]

        while p < q:
            if self._checkPalindrome(s, p, q):
                res = s[p:q+1] if q+1-p>len(res) else res
            qq = q -1
            while p < qq:
                if self._checkPalindrome(s, p, qq):
                    res = s[p:qq+1] if  qq+1 - p > len(res) else res
                qq -= 1
            pp = p + 1
            while pp < q:
                if self._checkPalindrome(s, pp, q):
                    res = s[pp:q+1] if q+1 - pp > len(res) else res
                pp += 1
            p += 1
            q -= 1

        return res

    def _checkPalindrome(self, s: str, p: int, q: int) -> bool:
        while p < q:
            if s[p] != s[q]:
                return False
            p += 1
            q -= 1
        return True


class Solution2:

    def longestPalindrome (self, s: str) -> str:
        if len(s) == 0:
            return ""
        res = s[0]
        for i in range(len(s) - 1):
            res1 = self._checkOddPalindrome(s, i, i)
            res2 = self._checkOddPalindrome(s, i, i+1)

            if len(res2) > len(res):
                res = res2
            if len(res1) > len(res):
                res = res1

        return res

    def _checkOddPalindrome(self, s: str, c1: int, c2: int) -> str:
        while c1 >= 0 and c2 <= len(s)-1 and s[c1] == s[c2]:
            c1 -= 1
            c2 += 1
        return s[c1 + 1: c2]


'''
字典标识法: 判断i,j之间是否是回文串 则 i-1, j+1 只需判断相等即可
'''


class Solution3:

    def longestPalindrome(self, s: str) -> str:
        lstart = 0
        lend = 0
        length = 0
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i):
                if s[j] == s[i] and ((i - j <= 2) or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > length:
                        length = i - j + 1
                        lstart = j
                        lend = i
        return s[lstart:lend + 1]


