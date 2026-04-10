class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## dynamic programing with 
        # mx= [0,0]
        # dp = [[0 for x in range(len(s)+1)] for y in range(len(s)+1)] 
        # print(len(dp),len(dp[0]))
        # for r in range(len(s)):
        #     for c in range(len(s)-r):
        #         result = 0
        #         #print(c,c+r,r,mx)
        #         print(s[c:c+r+1],c+1,c+r-1)
        #         if c ==c+r or (c+1<len(s) and s[c] == s[c+r]  and (r<=2 or dp[c+1][c+r-1]==1)):
                    
        #             result = 1
        #             if  mx[1]-mx[0]< r:
        #                 mx[0] = c
        #                 mx[1] = c+r
        #         dp[c][c+r] = result
       
        # return s[mx[0]:mx[1]+1]
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
