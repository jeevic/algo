
"""
https://leetcode.cn/problems/freedom-trail/

"""


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        char_to_index = {}
        self.mem = {}
        r_len = len(ring)
        for i in range(r_len):
            char = ring[i]
            if char_to_index.get(char, None) is None:
                char_to_index[char] = [i]
            else:
                char_to_index[char].append(i)
        return self.dp(char_to_index, ring, 0, key, 0)


    mem = {}
    def dp(self, char_to_index, ring, i, key, j):
        r_len = len(ring)
        k_len = len(key)

        if j == k_len:
            return 0

        if self.mem.get((i,j), None) is not None:
            return self.mem.get((i,j))

        char = key[j]
        res = sys.maxsize
        for index in char_to_index[char]:
            turn = abs(index - i)
            # 左转 右转
            turn = min(turn, r_len - turn)
            sub_problem = self.dp(char_to_index, ring, index, key, j+1)
            res = min(res, 1 + turn + sub_problem)
        self.mem[(i,j)] = res
        return res
