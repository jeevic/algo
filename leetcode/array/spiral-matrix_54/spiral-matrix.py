class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        x1 = 0
        y1 = 0
        x2 = m - 1
        y2 = n -1

        result = []
        while x1 <= x2 and y1 <= y2:
            if x1 == x2 and y1 == y2:
                result.append(matrix[x1][y1])
            elif x1 == x2 and y1 <= y2:
                i = y1
                while i <= y2:
                    result.append(matrix[x1][i])
                    i += 1
            elif x1 < x2  and y1 == y2:
                 i = x1
                 while i <= x2:
                     result.append(matrix[i][y1])
                     i += 1
            else:
                sr = self.printCircle(matrix, x1, y1, x2, y2)
                if len(sr) > 0 :
                    result.extend(sr)
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return result

    def printCircle(self, matrix, x1, y1, x2, y2) -> List[int]:
        le = []

        start = y1
        end = y2
        while start < end:
            le.append(matrix[x1][start])
            start += 1

        start = x1
        end = x2
        while start < end:
            le.append(matrix[start][y2])
            start += 1

        start = y2
        end = y1
        while start > end:
            le.append(matrix[x2][start])
            start -= 1

        start = x2
        end = x1
        while start > end:
            le.append(matrix[start][y1])
            start -= 1

        return le


