class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for i in range(n)]
        x1 = 0
        y1 = 0
        x2 = n -1
        y2 = n -1

        num = 0
        while num < n * n:
            if x1 <= x2:
                i = y1
                while i <= y2:
                    num = num + 1
                    matrix[x1][i] = num
                    i += 1
                x1 += 1

            if y1 <= y2:
                i = x1
                while i <= x2:
                    num = num + 1
                    matrix[i][y2] = num
                    i+= 1
                y2 -= 1
            if x1 <= x2:
                i = y2
                while i >= y1:
                    num = num + 1
                    matrix[x2][i] = num
                    i -= 1
                x2 -= 1

            if y2 >= y1:
                i = x2
                while i >= x1:
                    num = num + 1
                    matrix[i][y1] = num
                    i -= 1
                y1 += 1
        return matrix
