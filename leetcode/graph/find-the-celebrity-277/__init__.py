"""
277. 搜寻名人
@see https://leetcode.cn/problems/find-the-celebrity/
@see https://labuladong.github.io/algo/2/22/57/
"""


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

def knows(a, b):
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            j = 0
            while j < n:
                if i == j:
                    j += 1
                    continue
                if not knows(j, i) or knows(i, j):
                    break
                j += 1
            if j == n:
                return i
        return -1


class Solution2:
    def findCelebrity(self, n: int) -> int:
        # a -> b True a know b  a is not Celebrity
        # b -> a True b know a  b is not Celebrity
        # b -> <- a True a,b kown each other  a, b is not Celebrity
        # a b a,b dont kown each other  a, b is not Celebrity
        pq = []
        for i in range(n):
            pq.append(i)

        while len(pq) > 1:
            a = pq.pop(0)
            b = pq.pop(0)

            ak = knows(a, b)
            bk = knows(b, a)
            if (ak and bk) or (not ak and not bk):
                pass
            elif ak or not bk:
                pq.append(b)
            else:
                pq.append(a)
        if len(pq) == 0:
            return -1
        a = pq.pop(0)
        for i in range(n):
            if a == i:
                continue
            if not knows(i, a) or knows(a, i):
                return -1
        return a


class Solution3:
    def findCelebrity(self, n: int) -> int:
        a = 0
        for i in range(1, n):
            if knows(a, i) or not knows(i, a):
                a = i

        for i in range(n):
            if a == i:
                continue
            if knows(a, i) or not knows(i, a):
                return -1
        return a