class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x,y in points:
            for x2,y2 in points:
                if x==x2 and y2 ==y:
                    continue
                d = abs(x-x2) + abs(y - y2)
                adj[(x,y)].append((x2,y2,d))
                adj[(x2,y2)].append((x,y,d))
        visit = set()
        tempx,tempy = points[0]
        h = [(0,tempx,tempy)]
        res = 0
        while h:
            d,x,y = heapq.heappop(h)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            res += d
            for nx,ny,nd in adj[(x,y)]:
                heapq.heappush(h,(nd,nx,ny))
        return res
