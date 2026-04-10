class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        def dfs(r,c):
            if  r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c] == '0':
                return 
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row,col)
                    res = res +1
        return res
