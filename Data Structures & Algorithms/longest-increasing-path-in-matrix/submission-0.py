class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}
        def dfs(r,c, prev):
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = 0
            dp[(r,c)] = max(dfs(r+1,c, matrix[r][c])+1,dp[(r,c)])
            dp[(r,c)] = max(dfs(r-1,c, matrix[r][c])+1,dp[(r,c)])
            dp[(r,c)] = max(dfs(r,c-1, matrix[r][c])+1,dp[(r,c)])
            dp[(r,c)] = max(dfs(r,c+1, matrix[r][c])+1,dp[(r,c)])
            return dp[(r,c)]
        res = 1
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res,dfs(r,c,-1))
        return res
                

