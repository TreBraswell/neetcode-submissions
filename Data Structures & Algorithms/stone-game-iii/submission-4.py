class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len( stoneValue)
        dp = [float("-inf")]* (n+1)
        dp[n] = 0
        for i in range(n,-1,-1):
            total = 0 
            for j in range(i,min(i+3,n)):
                total += stoneValue[j]
                dp[i] = max(dp[i], total- dp[j+1])
        r = dp[0]
        if r== 0:
            return "Tie"
        elif r>0:
            return "Alice"
        else:
            return "Bob"