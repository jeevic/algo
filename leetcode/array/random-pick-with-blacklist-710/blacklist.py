
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        nums = [i for i in range(n)]
        not_black_nums = []
        for i in nums:
            if i not in blacklist:
                not_black_nums.append(i)
        self.nums = not_black_nums

    def pick(self) -> int:
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

class Solution1:

    def __init__(self, n: int, blacklist: List[int]):
        bl_len = len(blacklist)
        wl = n - bl_len

        black_map = {}
        for v in blacklist:
            black_map[v] = True

        last = n - 1
        for v in blacklist:
            if v >= wl:
                continue
            while last in black_map:
                last -= 1
            black_map[v] = last
            last -= 1

        self.black_map = black_map
        self.wl = wl

    def pick(self) -> int:
        idx = random.randint(0, self.wl - 1)
        if idx in self.black_map:
            return self.black_map[idx]
        return idx
