class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        wordDict = set(wordDict)
        def backtrack(i):
            if i == len(s):
                return [""]
            if i in dp:
                return dp[i]
            res = []
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w not in wordDict:
                    continue
                strings = backtrack(j+1)
                for string in strings:
                    sen = w
                    if string:
                        sen += ' ' + string
                    res.append(sen)
            dp[i] = res
            return res
        return backtrack(0)