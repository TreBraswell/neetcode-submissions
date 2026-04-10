class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = {}
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in adj:
                    queue = []
                    queue.append((r,c))
                    while queue:
                        row,col = queue.pop(0)
                        if row in range(0,len(grid)) and col in range(0, len(grid[0])) and (row,col) not in adj and grid[row][col] == '1':
                            adj[(row,col)] = 0
                            
                            queue.append((row+1,col))
                            queue.append((row-1,col))
                            queue.append((row,col+1))
                            queue.append((row,col-1))
                    islands +=1
        return islands

