class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx= [0,0]
        
        dp = [[0 for x in range(len(s)+1)] for y in range(len(s)+1)] 
        print(len(dp),len(dp[0]))
        for r in range(len(s)):
            for c in range(len(s)-r):
                result = 0
                #print(c,c+r,r,mx)
                print(s[c:c+r+1],s[c],s[c+r],c+1<len(s),c+r,c-1)
                if c ==c+r or (c+1<len(s) and s[c] == s[c+r]  and (r<=2 or dp[c+1][c+r-1]==1)):
                    
                    result = 1
                    if  mx[1]-mx[0]< r:
                        mx[0] = c
                        mx[1] = c+r
                dp[c][c+r] = result
        print(dp)
        return s[mx[0]:mx[1]+1]