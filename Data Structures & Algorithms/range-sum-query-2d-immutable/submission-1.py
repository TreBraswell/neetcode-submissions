class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.m = [[0 for c in range(COLS+1)] for r in range(ROWS+1)]
        for r in range(ROWS):
            for c in range(COLS):
                self.m[r+1][c+1] = matrix[r][c] + (self.m[r][c+1] + self.m[r+1][c] ) - self.m[r][c]

        print(self.m)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tl = self.m[row1][col1]
        tr = self.m[row1][col2+1]
        bl = self.m[row2+1][col1]
        br = self.m[row2+1][col2+1]
        return br - tr - bl + tl


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)