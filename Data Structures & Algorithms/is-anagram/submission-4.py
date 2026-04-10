class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_d[s[i]] = s_d.get(s[i],0) +1
            t_d[t[i]] = t_d.get(t[i],0) +1
        print(s_d,t_d)
        for i in s_d.keys():
            if i not in t or s_d[i] != t_d[i]:
                return False
        return True