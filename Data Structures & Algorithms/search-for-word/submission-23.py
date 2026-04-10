class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        def backtrack (r,c, curr_word):
            print(r,c,curr_word)
            if curr_word == word:
                return True
            if (r,c) in visit or r not in range(ROWS) or c not in range(COLS) or len(curr_word) >len(word) or (curr_word != "" and curr_word[-1] != word[len(curr_word)-1]):
                return False

            visit.add((r,c))
            t= backtrack(r+1,c,curr_word +board[r][c] ) or backtrack(r-1,c,curr_word+board[r][c]) or backtrack(r,c+1,curr_word+board[r][c]) or backtrack(r,c-1,curr_word+board[r][c])
            visit.remove((r,c))
            if t:
                return t
            
            # b = backtrack(r+1,c,curr_word) or \
            #     backtrack(r-1,c,curr_word) or \
            #     backtrack(r,c+1,curr_word) or \
            #     backtrack(r,c-1,curr_word)
            
            # return t or b
        for r in range(ROWS):
            for c in range(COLS):
                if  backtrack(r,c,""):
                    return True   
        return False