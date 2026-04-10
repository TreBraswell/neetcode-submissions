class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def recur(paren,sta):
            if len(paren) == n*2 and len(sta) ==0:
                res.append(paren)
                return 
            if len(paren) > n*2:
                return
            if len(sta) > 0:
                # sort6 out verification in a sec
                temp = sta.pop()
                recur(paren+ ")",sta)
                sta.append(temp)

            sta.append("(")
            recur(paren + "(",sta)
            sta.pop()
        recur("",[])
        return res

