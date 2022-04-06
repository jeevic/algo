from typing import List


class Solution:
    '''两数之和'''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p= 0
        q=len(numbers) - 1

        while p < q:
            sum1 = numbers[p] + numbers[q]
            if sum1 < target:
                p = p + 1
            elif sum1 > target:
                q = q - 1
            else:
                return [p + 1, q + 1]

        return []



