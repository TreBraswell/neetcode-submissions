class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        been_there = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r not in range(0,rows) or c not in range(0,cols) or (r,c) in been_there or board[r][c] != word[i]:
                return False
            been_there.add((r,c))
            res = (dfs(r+1,c,i+1) or
                  dfs(r-1,c,i+1) or
                  dfs(r,c+1,i+1) or
                  dfs(r,c-1,i+1))
            been_there.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
