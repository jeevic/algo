
# 优先级队列实现 优先级队列（Priority Queue)
# 最大堆
# @see https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484495&idx=1&sn=bbfeba9bb5cfd50598e2a4d08c839ee9&scene=21#wechat_redirect


class MaxPQ:

    def __init__(self, cap):
        self.cap = cap
        self.pq = [0 for i in range(self.cap + 1)]
        self.c = 0

    def max(self):
        return self.pq[1]

    def insert(self, key):
        if self.c >= self.cap:
            return
        self.c += 1
        self.pq[self.c] = key
        self.swim(self.c)
        return

    def del_max(self):
        e = self.pq[1]
        self.exch(1, self.c)
        self.pq[self.c] = 0
        self.c -= 1
        self.sink(1)
        return e

    def parent(self, key):
        return key // 2

    def left(self, key):
        return key * 2

    def right(self, key):
        return key * 2 + 1

    def less(self, i, j):
        return True if self.pq[i] < self.pq[j] else False

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def sink(self, key):

        while self.left(key) <= self.c:
            nxt = self.left(key)
            if self.right(key) <= self.c and self.less(nxt, self.right(key)):
                nxt = self.right(key)
            if self.less(nxt, key):
                break
            self.exch(key, nxt)
            key = nxt

    def swim(self, key):
        while key > 1 and self.less(self.parent(key), key):
            p = self.parent(key)
            self.exch(key, p)
            key = p
        return key


if __name__ == '__main__':
    pq = MaxPQ(5)
    pq.insert(1)
    print(pq.pq)
    pq.insert(3)
    print(pq.pq)
    pq.insert(4)
    print(pq.pq)
    pq.insert(5)
    print(pq.pq)
    print(pq.del_max())
    print(pq.pq)
