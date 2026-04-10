class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
        
        # row = {}
        # column = {}
        # for i in range(0,10):
        #     row[i] = {}
        #     column[i] = {}
        # r = 0
        # c = 0
        # box= {}
        # while r<9:
            
        #     for r in range(r,r+3):
                
        #         for c in range(c,c+3):

        #             if board[r][c] == ".":
        #                 continue
        #             if board[r][c] in box:
        #                 print('box',r,c,box)
        #                 return False
        #             box[board[r][c]] = True
        #             if board[r][c] in row[r]:
        #                 print('boardr')
        #                 return False
        #             row[r].update({board[r][c]:True})
        #             if board[r][c] in column[c]:
        #                 print('boardc')
        #                 return False
        #             column[c].update({board[r][c]:True})
        #         c= c+3
        #         if c>8:
        #             c= 0
        #     r= r+3
        #     box= {}
        # print(row)
        # print(column)
        # return True