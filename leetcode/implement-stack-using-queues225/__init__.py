"""
 用队列实现栈:
  思路就是队列直接循环吧
"""

class MyStack:

    def __init__(self):
        self.q = []
        self.top_e = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_e = x
        return

    def pop(self) -> int:
        length = len(self.q)
        if length >= 2:
            i = 0
            while i < length - 2:
                self.q.append(self.q.pop(0))
                i += 1
            x = self.q.pop(0)
            self.q.append(x)
            self.top_e = x
        else:
            self.top_e = None

        return self.q.pop(0)

    def top(self) -> int:
        return self.top_e

    def empty(self) -> bool:
        return True if len(self.q) == 0 else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()