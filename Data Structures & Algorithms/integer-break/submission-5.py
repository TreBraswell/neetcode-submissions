class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] *(n+1)
        dp[1] = 1

        for i in range(2,n+1):
            if i == n:
                dp[i] = 0
            else:
                dp[i] = i
            for j in range(i):
                r = dp[i-j] * dp[j]
                dp[i] = max(r,dp[i])
        return dp[n]

