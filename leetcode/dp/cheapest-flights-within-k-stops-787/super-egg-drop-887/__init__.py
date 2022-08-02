"""
  高楼扔鸡蛋
  最坏情况下 最小操作次数
  状态是鸡蛋  选择楼层

"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        self.mem = {}
        return self.dp(k, n)

    mem = {}

    def dp(self, k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k, n) in self.mem:
            return self.mem[(k, n)]

        res = sys.maxsize
        for f in range(1, n + 1):
            # 最坏情况下的最少次数
            res = min(res, max(
                # 碎了
                self.dp(k - 1, f - 1),
                # 没碎
                self.dp(k, n - f)
            ) + 1
                      )

        self.mem[(k, n)] = res
        return res


"""
 二分搜索优化
"""
class Solution:

    def superEggDrop(self, k: int, n: int) -> int:
        self.mem = {}
        return self.dp(k, n)

    mem = {}

    def dp(self, k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k, n) in self.mem:
            return self.mem[(k, n)]

        res = sys.maxsize
        # 用二分搜索代替线性搜索
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = self.dp(k - 1, mid - 1)  # 碎
            not_broken = self.dp(k, n - mid)  # 没碎
            # res = min(max(碎，没碎) + 1)
            if broken > not_broken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, not_broken + 1)
        self.mem[(k, n)] = res
        return res
