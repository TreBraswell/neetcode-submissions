class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[ 0 for c in range(len(s)+1)] for r in range(len(s)+1)]
        res = ''
        for c in range(len(s)):
            for r in range(len(s)-c):
                if c <=0:
                    #print('went here')
                    dp[r][c+r] = 1
                elif c==1 and  s[c+r] == s[r]:
                    dp[r][c+r] = 1
                elif s[c+r] == s[r] and dp[r+1][c+r-1] ==1:
                    #print('went here2')
                    dp[r][c+r] = 1
                if dp[r][c+r] ==1 and len(s[r:c+r+1]) > len(res):
                    #print(r,c+1,r,c+r)
                    #print('here')
                    res = s[r:c+r+1]
                #print(r,c+r,c,res)
                
        #print(dp)
        return res

        