

class Solution:

    def numTrees(self, n: int) -> int:
        return self.bulid(1, n)

    mem = {}

    def bulid(self, start, end):
        if start >= end:
            return 1
        s = "{}-{}".format(start, end)
        c = self.mem.get(s, None)
        if c is not None:
            return self.mem.get(s)
        res = 0
        i = start
        while i <= end:
            left = self.bulid(start, i-1)
            right = self.bulid(i+1, end)
            i += 1
            res += left * right
        self.mem[s] = res
        return res
