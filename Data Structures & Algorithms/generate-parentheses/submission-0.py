class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_count,closed_count,word):
            print(word,open_count,closed_count)
            if closed_count > open_count:
                return
            if closed_count > n or open_count > n:
                return    
            if closed_count == n and open_count == n:
                res.append(word)
                return
            
            backtrack(open_count,closed_count+1,word+')')
            backtrack(open_count+1,closed_count,word+'(')
        backtrack(1,0,'(')
        return res