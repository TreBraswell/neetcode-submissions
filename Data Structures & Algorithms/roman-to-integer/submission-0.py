class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50, "C":100, "D":500, "M": 1000}
        res = 0
        skip = False
        for i in range(len(s)-1,-1,-1):
            print(i,s[i])
            if skip:
                skip= False
                continue

            if i>0 and d[s[i]]> d[s[i-1]]:
                res += d[s[i]] - d[s[i-1]]
                skip = True
                continue
            res += d[s[i]]
        return res
    
