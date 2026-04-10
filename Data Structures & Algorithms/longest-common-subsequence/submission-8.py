class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dynamic programing
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
        ##fully recursive function doesnt work becuase you need to keep track of too many variables
        # def recur(text1,text2,i,j):
        #     # print(text1,text2,i,j)
        #     if i >len(text1)-1 or j >len(text2)-1: 
        #         return 0
        #     if text1[i] == text2[j]:
        #         if i == len(text1)-1 and j== len(text2)-1:
        #             return 1
        #         return 1 + recur(text1,text2,i+1,j+1)
        #     else:
        #         return max(recur(text1,text2,i,j+1), recur(text1,text2,i+1,j))
        # if len(text1)> len(text2):
        #     temp = text1
        #     text1 = text2
        #     text2 = temp
        # else:
        #     temp = text2
        #     text2 = text1
        #     text1 = temp
        # print(text1,text2)
        # return recur(text1,text2,0,0)
        