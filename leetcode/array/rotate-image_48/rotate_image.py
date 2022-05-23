class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while i <= n // 2 + 1:
            x1, y1 = i, i
            x2, y2 = n - 1 - i, n - 1 - i
            if x1 >= x2 and y1 >= x2:
                break
            self.rotate_circle(matrix, x1, y1, x2, y2)
            i += 1
        return

    def rotate_circle(self, matrix: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> None:
        start = 0
        end = x2 - x1
        while start < end:
            matrix[x1 + start][y2], matrix[x2][y2 - start], matrix[x2 - start][y1], matrix[x1][y1 + start] \
                = matrix[x1][y1 + start], matrix[x1 + start][y2], matrix[x2][y2 - start], matrix[2 - start][y1]
            start += 1
        return None



class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while i < n:
            j = i
            while j < n:
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                j += 1
            i+=1
        i = 0
        while i < n:
            j=0
            k = n -1
            while j < k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
            i += 1
        return matrix

