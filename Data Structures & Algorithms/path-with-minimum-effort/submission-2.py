class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        visited = set()
        h = []
        heapq.heappush(h,(0,0,0))
        r = float('inf')
        while h:
            # print(h)
            s,x,y = heapq.heappop(h)
            
            if x == ROWS-1 and y == COLS-1:
                r = min(r,s)
                continue
            if (x,y) in visited or x not in range(ROWS) or y not in range(COLS):
                continue
            visited.add((x,y))
            for xx,yy in moves:
                nx = xx+x
                ny = y +yy
                if nx not in range(ROWS) or ny not in range(COLS):
                    continue
                ns = max(s,abs(heights[x][y]-heights[nx][ny]))
                heapq.heappush(h,(ns,nx,ny))
        return r
                