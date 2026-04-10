class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        
        def loop_board(r1,c1):
            print(r1,c1)
            cur = set()
            for r in range(r1,r1+3):
                for c in range(c1,c1+3):
                    curr_num = board[r][c]
                    #print(cur,cols,rows)
                    if curr_num in cur or curr_num in cols[c] or curr_num in rows[r]:
                        print('this is it', r,c)
                        return False
                    if curr_num == '.':
                        continue
                    cur.add(curr_num)
                    cols[c].add(curr_num)
                    rows[r].add(curr_num)
            return True
        print(len(board))
        for r in range(0,len(board),3):
            for c in range(0,len(board[0]),3):
                if not loop_board(r,c):
                    return False
        return True