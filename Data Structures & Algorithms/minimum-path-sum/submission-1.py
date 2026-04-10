class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        r_b = [[float('inf') for r in range(COLS+1)] for c in range(ROWS+1)]
        print(r_b)
        r_b[ROWS][COLS-1] = 0
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                r_b[r][c] = grid[r][c]+ min(r_b[r+1][c],r_b[r][c+1])
        print(r_b)
        return r_b[0][0]