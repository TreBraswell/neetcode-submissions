class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        expand = []
        def add_pos(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c] != 2147483647:
                return
            visited.add((r,c))
            expand.append((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    expand.append((r,c))
                    visited.add((r,c))
        dist = 0
        while expand:
            for i in range(len(expand)):
                r,c = expand.pop(0)
                grid[r][c] = dist
                add_pos(r+1,c)
                add_pos(r-1,c)
                add_pos(r,c+1)
                add_pos(r,c-1)
            dist +=1
            

                