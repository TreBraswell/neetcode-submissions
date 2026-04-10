class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        for i in range(1,amount+1):
            for c in coins:
                if c == i:
                    dp[i] = 1
                    break
                if i-c >-1 and dp[i-c]!= 0:
                    if dp[i]==0:
                        dp[i] = dp[i-c] + dp[c]
                    else:
                        dp[i] = min(dp[i],dp[i-c] + dp[c])
        print(dp)
        if dp[amount] == 0 and amount != 0:
            return -1
        return dp[amount]
                    

            