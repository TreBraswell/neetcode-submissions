class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0
        for i in range(k+1):
            tempcosts = costs.copy()
            for s, d, c in flights:
                if costs[s] == float("inf"):
                    continue
                if costs[s] + c < tempcosts[d]:
                    tempcosts[d] = costs[s] + c
            costs = tempcosts
        if costs[dst] == float("inf"):
            return -1
        return costs[dst]
        
        # loop k +1 times
