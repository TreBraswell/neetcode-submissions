class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        found = set()
        while r<len(s):
            if s[r] in found:
                while s[r] in found:
                    found.remove(s[l])
                    l+=1
                found.add(s[r])

            else:
                found.add(s[r])

            r+=1
            res = max(res,r-l)
        return res
            
                