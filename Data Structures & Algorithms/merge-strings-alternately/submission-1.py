class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rl = min(len(word1),len(word2))


        res = ''
        for i in range(rl):
            res += word1[i] + word2[i]
        if len(word1)>len(word2):
            res += word1[rl:]
        else:
            res += word2[rl:]

        return res