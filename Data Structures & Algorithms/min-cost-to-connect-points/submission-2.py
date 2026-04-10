class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                
                dist = abs(points[i][0]- points[j][0]) + abs(points[i][1]- points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        visit = set()
        res = 0
        min_h = [[0,0]]
        while min_h:
            h = heapq.heappop(min_h)
            if h[1] in visit:
                continue
            res +=h[0]
            visit.add(h[1])

            if len(visit) == len(points):
                return res
            for i in adj[h[1]]:
                heapq.heappush(min_h,i)