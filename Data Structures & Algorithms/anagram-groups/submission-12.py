class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            arr = [0] *26
            for letter in strs[i]:
                arr[ord(letter)-ord('a')] +=1
            res[tuple(arr)].append(strs[i])
        return res.values()
                
