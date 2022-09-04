
"""
单调栈
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        i = length - 1
        res = [0 for i in range(length)]
        stack = []
        while i >= 0:
            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            res[i] = stack[-1] - i if len(stack) > 0 else 0
            stack.append(i)
            i -=1
        return res
