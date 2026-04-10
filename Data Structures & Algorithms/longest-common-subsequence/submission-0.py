class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)> len(text2):
            temp = text1
            text1 = text2
            text2 = temp
        else:
            temp = text2
            text2 = text1
            text1 = temp
        dp =  [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in dp:
            print(i)
        print(len(dp),len(dp[0]))

        for r in range(len(dp)-2,-1,-1):
            for c in range(len(dp[0])-2,-1,-1):
                print(c,r)
                print(len(text1),len(text2))
                if text1[c] == text2[r]:
                    dp[r][c]= 1 + dp[r+1][1+c]
                else:
                    dp[r][c]=max(dp[r][1+c],dp[1+r][c])
        return dp[0][0]