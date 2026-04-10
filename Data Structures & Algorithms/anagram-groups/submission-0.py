class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if d.get(s,None):
                d[s].append(strs[i])
                
            else:
                d[s] = [strs[i]]
        print(list(d.values()))
        return list(d.values())


            