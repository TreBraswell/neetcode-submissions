class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        def backtrack(i,s):
            if len(s) == k:
                self.res.append(s.copy())
                return
            if i >n:
                return 
            s.append(i)
            backtrack(i+1,s)
            s.pop()
            backtrack(i +1,s)
        backtrack(1,[])
        return self.res