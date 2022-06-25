# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

'''
 循环 + 堆栈思路
'''
class NestedIterator:
    stack = []

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for n in nestedList:
            if n.isInteger() is False:
                if len(n.getList()) <= 0:
                    continue
            self.stack.insert(0, StackNode(n, 0))

    def next(self) -> int:
        stn = self.stack.pop()
        nst = stn.get_nst()
        return nst.getInteger()

    def hasNext(self) -> bool:
        while len(self.stack) > 0:
            stn = self.stack.pop()
            nst = stn.get_nst()
            if nst.isInteger():
                self.stack.append(stn)
                return True
            if len(nst.getList()) <= 0:
                continue
            nst_list = nst.getList()[stn.get_pos()]
            if len(stn.get_nst().getList()) - 1 > stn.get_pos():
                stn.set_pos(stn.get_pos() + 1)
                self.stack.append(stn)
            if nst_list.isInteger():
                self.stack.append(StackNode(nst_list, 0))
                return True
            else:
                self.stack.append(StackNode(nst_list, 0))
        return False


class StackNode:
    def __init__(self, nestedList: [NestedInteger], pos):
        self.nst = nestedList
        self.pos = pos

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def get_nst(self):
        return self.nst
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# 递归思想


class NestedIterator:
    link_list = []

    def __init__(self, nestedList: [NestedInteger]):
        for ni in nestedList:
            self.traverse(ni)

    def next(self) -> int:
        return self.link_list.pop(0)

    def hasNext(self) -> bool:
        return True if len(self.link_list) > 0 else False

    def traverse(self, nsti):
        if nsti.isInteger():
            self.link_list.append(nsti)
            return
        for ni in nsti.getList():
            self.traverse(ni)

# 循环思想

class NestedIterator:
    nst = []

    def __init__(self, nestedList: [NestedInteger]):
        for ni in nestedList:
            self.nst.append(ni)

    def next(self) -> int:
        ni = self.nst.pop(0)
        return ni.getInteger()

    def hasNext(self) -> bool:
        while len(self.nst) > 0:
            if self.nst[0].isInteger():
                return True
            sub_nst = self.nst.pop(0).getList()
            length = len(sub_nst)
            i = length - 1
            while i >= 0:
                self.nst.insert(0, sub_nst[i])
                i -= 1
        return False
