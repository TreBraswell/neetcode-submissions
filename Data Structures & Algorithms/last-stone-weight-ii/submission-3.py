class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sm = sum(stones)
        goal = math.ceil(sm/2)
        dp = {}
        def dfs(i,total):
            if total >= goal or i == len(stones):
                return abs(total - (sm-total))
            if (i,total) in dp:
                return dp[(i,total)]
            dp[(i,total)] = min(dfs(i+1,total),dfs(i+1,total+stones[i]))
            return dp[(i,total)]
        return dfs(0,0)