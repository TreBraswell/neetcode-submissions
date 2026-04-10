class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        res = 0
        my_dict = {}
        while r<len(s):
            print(l,r,my_dict)
            if s[r] in my_dict:
                while s[r] in my_dict:
                    my_dict.pop(s[l],None)
                    l+=1
            my_dict[s[r]] = True
            r+=1
            res = max(res,r-l)

            
        return res