class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0 for i in range(length)]
        for l in updates:
            start = l[0]
            end = l[1]
            val = l[2]
            diff[start] = diff[start] + val
            if end + 1 < length:
                diff[end + 1] = diff[end+1] - val
        r = self.result(diff)
        return r

    def result(self, diff: List[int]) -> List[int]:
        length = len(diff)
        result = [ 0 for i in range(length)]
        result[0] = diff[0]

        idx = 1
        while idx < length:
            result[idx] = result[idx - 1] + diff[idx]
            idx +=1
        return result

