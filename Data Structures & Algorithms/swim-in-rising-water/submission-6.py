class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions =[[0,1],[0,-1],[1,0],[-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        h_q = [(grid[0][0],(0,0))]
        while h_q:
            s,c = heapq.heappop(h_q)
            x,y = c
            if(x,y) in visit: 
                continue
            if x == ROWS-1 and y == COLS-1:
                return s
            visit.add((x,y))
            for x1,y1 in directions:
                x2 = x1 +x
                y2 = y1 + y
                if x2 not in range(ROWS) or y2 not in range(COLS):
                    continue
                heapq.heappush(h_q,(max(s,grid[x2][y2]),(x2,y2)))

        