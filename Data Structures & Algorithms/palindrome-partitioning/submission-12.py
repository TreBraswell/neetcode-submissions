class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def ispal(pali):
            l = 0
            r = len(pali)-1
            while l<=r:
                if pali[l] != pali[r]:
                    return False
                l +=1
                r -= 1
            return True
        
        def dfs(idx,curr):
            if idx == len(s):
                res.append(curr.copy())
                return 
            for i in range(idx,len(s)):
                if ispal(s[idx:i+1]):
                    curr.append(s[idx:i+1])
                    dfs(i +1,curr)
                    curr.pop()
        dfs(0,[])
        return res
