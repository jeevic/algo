"""
 Union-Find 算法，也就是常说的并查集（Disjoint Set）结构，主要是解决图论中「动态连通性」问题
 如: 无向图中连通分量的数目」
"""


class UnionFind:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]

    """
      联通两个节点
      将两个节点父节点联通
    """
    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_p == parent_q:
            return
        self._parent[parent_p] = parent_q
        self._count -= 1

    """
     判断两个节点是否联通, 判断两个节点的父节点是否相等即可
    """
    def connected(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)
        if parent_q == parent_p:
            return True
        return False
    """
      获取节点的父节点
    """
    def find(self, x):
        """
           优化方案一: 所有节点和父节点指向同一父节点
            while self._parent[x] != x:
                self._parent[x] = self._parent[self._parent[x]]
                x = self._parent[x]
        """
        while self._parent[x] != x:
            # x = self._parent[x]
            """
              优化方案二: 所有节点指向根节点 完全打平
            """
            self._parent[x] = self.find(self._parent[x])
            x = self._parent[x]

        return self._parent[x]
    """
      获取节点数量
    """
    def count(self):
        return self._count


if __name__ == '__main__':
    uf = UnionFind(10)
    print("uf count: {}".format(uf.count()))
    uf.union(1, 5)
    print("uf count: {}".format(uf.count()))
    print("connected 1 and 5 {}".format(uf.connected(1, 5)))
    uf.union(1, 5)
    print("uf count: {}".format(uf.count()))
    print("connected 1 and 5 {}".format(uf.connected(1, 5)))
    uf.union(1, 8)
    print("uf count: {}".format(uf.count()))
    print("connected 1 and 8 {}".format(uf.connected(1, 8)))
