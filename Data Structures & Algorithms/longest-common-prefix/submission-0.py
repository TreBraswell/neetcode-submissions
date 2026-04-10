class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for r in range(len(strs[0])):
            for i in range(len(strs)):
                word = strs[i]
                if len(word)-1<r or (i>0 and word[r] !=  strs[i-1][r]):
                    return word[0:r]
        return strs[0]