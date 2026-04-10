class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pr = [float('inf')] * n
        pr[src] = 0 
        for i in range(k+1):
            t = pr.copy()
            for s,d,p in flights:
                if pr[s] == float('inf'):
                    continue
                if pr[s] + p < t[d]:
                    t[d] = pr[s] + p
            pr = t
        return pr[dst] if pr[dst] != float('inf') else -1