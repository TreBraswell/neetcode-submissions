class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []
        self.curr = ""

        res = []
        nums = { '2':"abc", '3': "def", '4':"ghi", '5':"jkl", '6':"mno", '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def dfs(i):
            if i == len(digits):
                res.append(self.curr)
                return 
            c = nums[digits[i]]
            for ii in c:
                self.curr = self.curr + ii 
                dfs(i+1)
                self.curr = self.curr[:-1]
        dfs(0)
        return res