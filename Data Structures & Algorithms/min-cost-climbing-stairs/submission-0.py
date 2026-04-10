class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-1,-1,-1):
            c1  = 0
            c2 = 0
            if i +2 < len(cost):
                c2 = cost[i+2]
            if i +1< len(cost):
                c1 = cost[i+1]
            cost[i] = min(cost[i] + c1, cost[i] + c2)
        return min(cost[0],cost[1])