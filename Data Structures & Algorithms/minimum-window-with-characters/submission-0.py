import copy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for i in range(len(t)):
           t_dict[t[i]] = t_dict.get(t[i],0) + 1
        s_dict = {}
        l = 0
        res = ''
        temp_dict = copy.deepcopy(t_dict)
        for r in range(len(s)):
            print(l,r,res,temp_dict,'this is : ',s_dict)
            if s[r] in t_dict:
                s_dict[s[r]] = s_dict.get(s[r],0) + 1
                print('this is : s_dict ',s_dict, temp_dict )
                if s[r] in temp_dict and s_dict[s[r]] == temp_dict[s[r]]:
                    temp_dict.pop(s[r])
                print('this is after : s_dict ',s_dict, temp_dict )
                if not temp_dict:
                    print('temp_dict')
                    while l<=r:
                        print('while loop')
                        if s[l] in s_dict:
                           s_dict[s[l]] = s_dict[s[l]] -1
                           

                           if s_dict[s[l]] < t_dict[s[l]]:
                                if len(res)> r-l or res == '':
                                    res = s[l:r+1]
                                print('this is res')
                                temp_dict = copy.deepcopy(t_dict)
                                for i in t_dict.keys():
                                    if s_dict[i] >= temp_dict[i]:
                                        temp_dict.pop(i)
                                l = l+1
                                break
                        l = l+1    
                        
        return res