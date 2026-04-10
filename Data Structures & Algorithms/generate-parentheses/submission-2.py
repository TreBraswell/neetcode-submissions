class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []
        def back(o,c):
            if o==c==n:
                res.append(''.join(s))
                return 

            if o< n:
                s.append('(')
                back(o+1,c)
                s.pop()
            if c<o:
                s.append(')')
                back(o,c+1)
                s.pop()
        back(0,0)
        return  res