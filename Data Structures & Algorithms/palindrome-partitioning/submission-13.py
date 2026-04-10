class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curr = []
        res = []

        def ispali(s,l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l +=1
                r-=1
            return True


        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return
            for j in range(i,len(s)):
                if ispali(s,i,j):
                    curr.append(s[i:j+1])
                    backtrack(j+1)
                    curr.pop()
        backtrack(0)
        return res    

