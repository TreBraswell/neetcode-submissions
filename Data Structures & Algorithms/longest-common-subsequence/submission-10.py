class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        ROWS = len(text1)
        COLS = len(text2)
        def dfs(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            if text1[r] == text2[c]:
                dp[(r,c)] = dfs(r+1,c+1) +1
            else:
                dp[(r,c)] = max(dfs(r+1,c), dfs(r,c+1))
            return dp[(r,c)]
        return dfs(0,0)
