class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        p = {
            '2' :'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
            }
        res = []
        def dfs(curr, i):
            if i == len(digits):
                res.append(curr[:])
                return
            for j in p[digits[i]]:
                print(j)
                curr = curr + j
                dfs(curr,i+1)
                curr = curr[:len(curr)-1]
        dfs('',0)
        if len(digits) == 0 or digits is None:
            return []
        return res