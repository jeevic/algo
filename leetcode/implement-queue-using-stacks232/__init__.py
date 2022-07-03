"""
用栈实现队列
"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        return

    def pop(self) -> int:
        e = self.peek()
        if e == None:
            return None
        return self.stack2.pop(0)

    def peek(self) -> int:
        if len(self.stack2) == 0:
            length = len(self.stack1)
            while length > 0:
                self.stack2.append(self.stack1.pop(0))
                length -= 1
        return self.stack2[0] if len(self.stack2) > 0 else None

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

