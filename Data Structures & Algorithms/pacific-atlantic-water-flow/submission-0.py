class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,water_set,pr,pc):
            if r not in range(rows) or c not in range(cols) or (r,c) in water_set or heights[r][c]<heights[pr][pc]:
                return
            water_set.add((r,c))
            dfs(r+1,c,water_set,r,c)
            dfs(r-1,c,water_set,r,c)
            dfs(r,c-1,water_set,r,c)
            dfs(r,c+1,water_set,r,c)
            
        for r in range(rows):
            dfs(r,0,pacific,r,0)
            dfs(r,cols-1,atlantic,r,cols-1)
        for c in range(cols):
            dfs(0,c,pacific,0,c)
            dfs(rows-1,c,atlantic,rows-1,c)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append((r,c))
        return res