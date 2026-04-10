class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s) +1)
        dp[0] =1
        if len(s)>0:
            if int(s[0]) == 0:
                dp[1] =0
            else:
                dp[1] = 1
        else:
            return 1
        for i in range(1,len(s)):
            print(dp)
            res = 0
            lon = int(s[i-1:i+1])
            print(lon)
            sho = int(s[i])
            if lon in range(10,27):
                #for dp difference with string
                res += dp[i+1-2]
            if sho in range(1,9+1):
                #for dp difference with string
                res += dp[i+1-1]
            dp[i+1] = res
        
        return dp[len(s)]