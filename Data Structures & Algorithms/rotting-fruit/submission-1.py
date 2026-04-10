class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        bs = 0

        expand = []
        def add_pos(r,c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] != 1 :
                return
            expand.append((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bs +=1
                if grid[r][c] == 2:
                    expand.append((r,c))
        time = -1
        while expand:
            for i in range(len(expand)):
                r,c = expand.pop(0)
                if grid[r][c] != 2:

                    grid[r][c] = 2
                    bs -=1
                add_pos(r+1,c)
                add_pos(r-1,c)
                add_pos(r,c+1)
                add_pos(r,c-1)
            time +=1
        print(bs)
        if bs >0:
            return -1
        return max(time,0)