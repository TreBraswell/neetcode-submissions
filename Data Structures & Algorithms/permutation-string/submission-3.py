class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for i in range(len(s1)):
           s1_dict[s1[i]] = s1_dict.get(s1[i],0) + 1
        s2_dict = {}
        l = 0
        for r in range(len(s2)):
            print(l,r)
            if s2[r] in s1_dict:
                if s2[l] not in s1_dict:
                    l=r
                s2_dict[s2[r]] = s2_dict.get(s2[r],0) + 1
                if s2_dict == s1_dict:
                    return True
                if s2_dict[s2[r]] > s1_dict[s2[r]]:
                    while l<r and s2_dict[s2[r]] > s1_dict[s2[r]]:
                        s2_dict[s2[l]] = s2_dict[s2[l]] -1

                        if s2_dict.get(s2[l],-1) == 0:
                            s2_dict.pop(s2[l])
                        l = l+1
                
            else:
                s2_dict = {}
                l = r


        return False
