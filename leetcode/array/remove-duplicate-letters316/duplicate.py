# same question
# https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = [0 for i in range(256)]
        for c in s:
            count[ord(c)] += 1

        in_stack = [False for i in range(256)]

        for c in s:
            count[ord(c)] -= 1
            if in_stack[ord(c)] is True:
                continue

            while len(stack) > 0 and ord(stack[-1]) > ord(c):

                if count[ord(stack[-1])] == 0:
                    break
                e = stack.pop()
                in_stack[ord(e)] = False

            stack.append(c)
            in_stack[ord(c)] = True

        return "".join(stack)
