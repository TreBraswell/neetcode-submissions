class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visits = set()
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visits and grid[r][c] == "1":
                    adj = []
                    adj.append((r,c))
                    islands +=1
                    while adj: 
                        row,col = adj.pop(0)
                        if row not in range(len(grid)) or col not in range(len(grid[0])) or (row,col) in visits or grid[row][col]!= "1":
                            continue
                        visits.add((row,col))
                        adj.append((row-1,col))
                        adj.append((row+1,col))
                        adj.append((row,col-1))
                        adj.append((row,col+1))
        return islands


            
