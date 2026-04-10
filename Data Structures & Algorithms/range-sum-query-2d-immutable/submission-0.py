class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(0,ROWS):
            for c in range(0,COLS):
                self.sumMat[r+1][c+1] = matrix[r][c] + (self.sumMat[r][c+1] + self.sumMat[r+1][c] - self.sumMat[r][c])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
         br = self.sumMat[row2+1][col2+1]
         tld = self.sumMat[row1][col1]
         bl = self.sumMat[row2+1][col1]
         tr = self.sumMat[row1][col2+1]
         return br - (bl+tr-tld)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)