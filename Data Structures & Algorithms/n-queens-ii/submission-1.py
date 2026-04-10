class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        neg_diag = set()
        pos_diag = set()
        self.res = 0
        def backtrack(r):
            if r ==n:
                self.res+=1
            for c in range(n):
                if c in cols or r+ c in pos_diag or r-c in neg_diag:
                    continue
                neg_diag.add(r-c)
                pos_diag.add(r+c)
                cols.add(c)
                backtrack(r+1)
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
        backtrack(0)
        return self.res


