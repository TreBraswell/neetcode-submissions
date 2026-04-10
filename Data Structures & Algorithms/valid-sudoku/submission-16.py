class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        for c in range(len(board[0])):
            cols[c] = set()
        for r in range(len(board)):
            rows[r] = set()
        def check_board(r_max,c_max):
            temp = set()
            for r in range(r_max-3,r_max):
                for c in range(c_max-3,c_max):
                    print("inner r c", r,c)
                    if board[r][c] in temp:
                        print("Failed in temp", temp)
                        return False
                    if board[r][c] in cols[c] or board[r][c] in rows[r]:
                        print("Failed in blah")
                        return False
                    if board[r][c] == ".":
                        continue
                    cols[c].add(board[r][c]) 
                    rows[r].add(board[r][c])
                    temp.add(board[r][c])
            return True
        
        for r in range(3,len(board[0])+1,3):
            for c in range(3,len(board[0])+1,3):
                print(r,c)
                if not check_board(r,c):
                    print(cols)
                    print(rows)
                    return False
        return True