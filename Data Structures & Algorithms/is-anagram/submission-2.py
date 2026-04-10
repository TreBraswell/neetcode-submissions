class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in s_d:
                s_d[s[i]] = 0
            else:
               s_d[s[i]] += 1 
            if t[i] not in t_d:
                t_d[t[i]] = 0
            else:
               t_d[t[i]] += 1 
        return s_d == t_d
