class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or board[r][c] != "O":
                return
            board[r][c] = "I"
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][cols-1] == "O":
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0,c)
            if board[rows-1][c] == "O":
                dfs(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "I":
                    board[r][c] = "O"
        
        
        # def dfs(r,c):
            
        #     if r not in range(rows) or c not in range(cols):
        #         return False
        #     if board[r][c] == "X":
        #         return True
        #     if (r,c) in visited:
        #         if board[r][c] == "X":
        #             return True
        #         else:
        #             return False
        #     visited.add((r,c))
        #     if dfs(r+1,c) and dfs(r-1,c) and dfs(r,c+1) and dfs(r,c-1):
        #         board[r][c] = 'X'
        #         return True
        #     else:
        #         return False
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == "O":
                    queue = ()
