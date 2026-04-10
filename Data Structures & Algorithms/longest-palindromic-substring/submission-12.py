class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        pali_board = [[0 for c in range(l)] for r in range(l)]
        mx_p = (0,0)
        for rr in range(l):
            for r in range(l):
                if r+rr not in range(l):
                    continue
                
                if r == r+rr:
                    pali_board[r][r+rr] = 1
                elif rr == 1:
                    if s[r] == s[r+rr]:
                        pali_board[r][r+rr] = 2
                else:
                    if s[r] == s[r+rr] and pali_board[r+1][r+rr-1]>0:
                        pali_board[r][r+rr] += pali_board[r+1][r+rr-1] + 1
                if pali_board[r][r+rr] >=  pali_board[mx_p[0]][mx_p[1]]:
                    mx_p = (r,r+rr)
        #         print(pali_board)
        # print(mx_p)
        return s[mx_p[0]:mx_p[1]+1]