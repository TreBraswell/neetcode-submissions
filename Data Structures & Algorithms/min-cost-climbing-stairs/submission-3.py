class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one = 0
        two = 0
        curr = 0
        for i in range(len(cost)):
            
            
            curr = min(one, two) + cost[i]
            print(curr,one,two)
            two = one
            one = curr
        return min(curr,one,two)
        dp = {}
        dp[-1] = 0
        dp[-2] = 0
        for i in range(len(cost)):
            dp[i] = min(dp[i-1]  ,dp[i-2]) + cost[i]

        return min(dp[len(cost)-1],dp[len(cost)-2])
        self.res = float('inf')
        def dfs(curr,i):
            if i >=len(cost):
                self.res = min(self.res,curr)
                return 
            if i !=-1:
                curr += cost[i]
            dfs(curr,i+1)
            dfs(curr,i+2)
        dfs(0,-1)
        return self.res