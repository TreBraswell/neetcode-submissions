class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        s = min(len(str1), len(str2))
        for r in range(s,-1,-1):
            n_str = str2[:r+1]
            if len(str1)%len(n_str) != 0 or len(str1)<len(n_str) or len(str2)%len(n_str) != 0 :
                continue
            t = str1
            while len(t)>0:
                if n_str != t[:r +1]:
                    break
                t = t[r+1:]
            if len(t) == 0:
                return n_str
        return ''