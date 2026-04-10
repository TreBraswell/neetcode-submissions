class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_dict = dict(Counter(t))
        t_dict_copy = t_dict.copy()
        s_dict = {}
        
        l = 0
        r = 0
        res = ''

        while r < len(s):
            print(l,r, ' ', s_dict, ' ', t_dict, ' ',t_dict_copy )
            if s[r] in t_dict:
                if s[r] not in s_dict:
                    s_dict[s[r]] = 0
                s_dict[s[r]] +=1
                if s[r] in t_dict_copy and t_dict_copy[s[r]] <= s_dict[s[r]]:
                    del t_dict_copy[s[r]]
                if len(t_dict_copy) <= 0: 
                    print(l,r)
                    
                    while True:
                        val = s[l]
                        if val in s_dict:
                            s_dict[val] -= 1
                            if s_dict[val] < t_dict[val]:
                                t_dict_copy[val] = t_dict[val]
                                if r - l < len(res) or res == "":
                                    res = s[l:r+1]
                                l+=1
                                break
                        l+=1
            r +=1
        return res