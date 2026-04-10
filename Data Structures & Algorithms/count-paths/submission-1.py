class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =  [[0 for i in range(n+1)] for j in range(m+1)]
        dp[m-1][n-1] = 1
        # for i in dp:
        #     print(i)
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                
                if r == m-1 and c == n-1:
                    continue
                # print(r+1,c+1)
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
                # print(r,c,dp)
        return dp[0][0]