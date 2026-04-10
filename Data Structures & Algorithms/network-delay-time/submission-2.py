class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for ui, vi, ti in times:
            
            adj[ui].append((vi,ti))
        visit = set()
        h_q = [(0,k)]
        res = 0
        while h_q:
            
            ti,ui = heapq.heappop(h_q)
            print('this is ti,ui',ti,ui)
            if ui in visit:
                continue
            
            visit.add(ui)
            if len(visit) == n:
                return ti
            for uii,tii in adj[ui]:
                
                heapq.heappush(h_q,(ti + tii,uii))
        
        
        return -1