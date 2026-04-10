class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS= len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if (r,c) in visit:
                return 0 
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c]==0:
                return 1
            visit.add((r,c))
            return dfs(r+1, c)+ dfs(r-1,c)+ dfs(r,c+1)+ dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]== 1:
                    return dfs(r,c)
