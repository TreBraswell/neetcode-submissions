class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        mx = 0
        sub = {}
        while r< len(s):
            if s[r] in sub:
                while s[r] in sub:
                    sub.pop(s[l])
                    l+=1
            else:
                
                sub[s[r]] = True
                r +=1
                mx = max(mx,r-l)
        return mx