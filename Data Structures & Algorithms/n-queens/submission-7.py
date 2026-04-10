class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        p_diag = set()
        n_diag = set()
        c_set = set()
        board = [[ '.' for _ in range(n)] for _ in range(n)]
        for row in board:
            print()
        res = []
        def dfs(r):
            if r ==n :
                temp =[]
                for row in board:
                    temp.append(''.join(row))
                res.append(temp)
                return 
            for c in range(n):
                if c in c_set or (r-c) in n_diag or (r+c) in p_diag:
                    continue
                board[r][c] = "Q"
                c_set.add(c)
                n_diag.add((r-c))
                p_diag.add((r+c))
                dfs(r+1)
                board[r][c] = '.'
                c_set.remove(c)
                n_diag.remove((r-c))
                p_diag.remove((r+c))
        dfs(0)
        return res
