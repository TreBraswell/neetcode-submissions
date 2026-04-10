class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        for i in t:
            if l== len(s):
                return True
            if i == s[l]:
                l+=1
                
        if l== len(s):
                return True            
        return False