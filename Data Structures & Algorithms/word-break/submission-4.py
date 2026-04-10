class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                # if i >0:
                #     print(dp, i,i+len(word),s[i:i+len(word)] )
                if i + len(word) < len(dp) and s[i:i+len(word)] == word and dp[i+len(word)]:
                    dp[i] = dp[i+len(word)]
                    break
        return dp[0]
