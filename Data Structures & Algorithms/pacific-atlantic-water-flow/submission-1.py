class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        p = set()
        def dfs(prevr,prevc,r,c,visit):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or heights[prevr][prevc] >heights[r][c]:
                print(r,c)
                return
            visit.add((r,c))
            dfs(r,c,r,c-1,visit)
            dfs(r,c,r,c+1,visit)
            dfs(r,c,r-1,c,visit)
            dfs(r,c,r+1,c,visit)
            

        for i in range(ROWS):
            dfs(i,0,i,0, p)
        for i in range(COLS):
            print(i)
            dfs(0,i,0,i, p)
        a =set()
        for i in range(ROWS):
            dfs(i,COLS-1,i,COLS-1, a)
        for i in range(COLS):
            dfs(ROWS-1,i,ROWS-1,i, a)
        
        print(a)
        print(p)
        return list(a.intersection(p))