class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # 计算每一行所有值纸盒

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        row = row1
        while row <= row2:
            col = col1
            while col <= col2:
                sum += self.matrix[row][col]
                col += 1
            row += 1
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        maxtrix_sums = {}
        # 计算每一行所有值累加值
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        while row < rows:
            col = 0
            while col < cols:
                col_v = col
                sum = 0
                key = "%d-%d" % (row,col)
                while col_v < cols:
                    sum += matrix[row][col_v]
                    key1="%s-%d" % (key,col_v)
                    maxtrix_sums[key1] = sum
                    col_v += 1
                col += 1
            row += 1
        print(maxtrix_sums)
        self.maxtrix_sums = maxtrix_sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        row = row1
        while row <= row2:
            key = "%d-%d-%d" % (row, col1, col2)
            sum += self.maxtrix_sums[key]
            row += 1
        return sum


class NumMatrix3:
    
    def __init__(self, matrix: List[List[int]]):
        # 计算(0,0)到(x,y)的和
        rows = len(matrix)
        cols = len(matrix[0])
        maxtrix_sums = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        row = 1
        while row <= rows:
            col = 1
            while col <= cols:
                maxtrix_sums[row][col] = maxtrix_sums[row - 1][col] + maxtrix_sums[row][col - 1] + matrix[row - 1][
                    col - 1] - maxtrix_sums[row - 1][col - 1]
                col += 1
            row += 1
        self.maxtrix_sums = maxtrix_sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.maxtrix_sums[row2 + 1][col2 + 1] - self.maxtrix_sums[row2 + 1][col1] - self.maxtrix_sums[row1][
            col2 + 1] + self.maxtrix_sums[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

