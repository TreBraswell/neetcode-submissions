class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # do bfs
        # have a minheap for the max of each level
        # check to see if out of board
        # return the first one that reaches the bottom
        minheap = [[0,(0,0)]]
        visit = set()
        R = len(grid)
        C = len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while minheap:
            t,p = heapq.heappop(minheap)

            r,c = p
            if r not in range(R) or c not in range(C) or (r,c) in visit:
                continue
            t = max(t,grid[r][c])
            if r == R-1 and c == C-1:
                return t
            visit.add((r,c))
            for x,y in directions:
                heapq.heappush(minheap,[t,(r+x,c+y)])
            
            