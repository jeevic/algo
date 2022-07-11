
class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        length = len(envelopes)
        if length == 1:
            return 1
        envelopes.sort(key=lambda x:x[0])

        dp = [1 for i in range(length)]
        index = 1
        while index < length:
            j = 0
            while j < index:
                if envelopes[j][0] == envelopes[index][0] or envelopes[j][1] >= envelopes[index][1]:
                    j += 1
                    continue
                dp[index] = max(dp[index], dp[j] + 1)
                j += 1
            index += 1
        return max(dp)


