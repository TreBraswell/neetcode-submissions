class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set()
        h = []
        ROWS = len(heights)
        COLS = len(heights[0])
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        heapq.heappush(h,(0,0,0))
        while h:
            d,x,y = heapq.heappop(h)
            if (x,y) == (ROWS-1,COLS-1):
                return d
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for xx,yy in moves:
                nx = x+xx
                ny = y + yy
                if nx not in range(ROWS) or ny not in range(COLS):
                    continue
                nd = max(d,abs(heights[x][y]-heights[nx][ny]))
                heapq.heappush(h,(nd,nx,ny))
            
            

        