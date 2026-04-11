class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        fill_top_row = False
        for i in range(COLS):
            if matrix[0][i] == 0:
                fill_top_row = True
        fill_top_col = False
        for i in range(ROWS):
            if matrix[i][0] == 0:
                fill_top_col = True
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] ==0:
                    matrix[r][c] = 0
        if fill_top_col:
                for i in range(ROWS):
                    matrix[i][0] = 0
        if fill_top_row:
            for i in range(COLS):
                matrix[0][i] = 0

        