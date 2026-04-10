class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if i >0 and ((int(s[i]) in range(10) and s[i-1] == '1') or (int(s[i]) in range(7) and s[i-1] == '2')):
                dp[i+1] += dp[i-1]
        return dp[len(s)]