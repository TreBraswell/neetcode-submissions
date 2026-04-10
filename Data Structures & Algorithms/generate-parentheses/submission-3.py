class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.curr = ""
        res = []
        def dfs(c,o):
            if c == 0 and o ==0:
                res.append(self.curr)
                return
            
            if o<c:
                self.curr = self.curr + ')'
                dfs(c-1,o)
                self.curr = self.curr[:-1]

            if o != 0:
                self.curr = self.curr + '('
                dfs(c,o-1)
                self.curr = self.curr[:-1]
        dfs(n,n)
        return res

