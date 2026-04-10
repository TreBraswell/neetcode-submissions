class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def inword(r,c,i):
            if i == len(word):
                return True
            if r not in range(len(board)) or c not in range(len(board[0])) or (r,c) in visited or (i< len(word) and board[r][c] != word[i]):
                return False
            if i >=len(word):
                return True
            visited.add((r,c))
            t = inword(r+1,c,i+1) or inword(r-1,c,i+1) or inword(r,c+1,i+1) or inword(r,c-1,i+1)
            visited.remove((r,c))
            return t
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if inword(r,c,0):
                    return True

        return False