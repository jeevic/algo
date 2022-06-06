

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        remain_len = len(num) - k
        stack = []
        if remain_len == 0:
            return "0"
        for c in num:
            while k > 0 and len(stack) > 0 and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        result = "".join(stack[:remain_len]).lstrip("0")
        if result == "":
            result = "0"
        return result
