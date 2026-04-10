class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit = []
        
        min_cost = list(zip(capital,profits))
        heapq.heapify(min_cost)
        for i in range(k):

            while min_cost and min_cost[0][0]<=w:
                c,p = heapq.heappop(min_cost)
                heapq.heappush(profit, -1*p)
            
            if profit:
                w = w + heapq.heappop(profit) *-1
        return w

