class Solution:
    def scoreOfString(self, s: str) -> int:
        r = 0
        for i in range(1,len(s)):
            print(i)
            r += abs(ord(s[i])-ord(s[i-1]))
        return r