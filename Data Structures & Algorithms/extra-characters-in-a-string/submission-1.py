class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {}
        words = set(dictionary)
        class TrieNode:
            def __init__(self):
                self.char = {}
                self.isword = False
        class Trie:
            def __init__(self,words):
                self.root = TrieNode()
                for word in words:
                    curr = self.root 
                    for w in word:
                        if w not in curr.char:
                            curr.char[w] = TrieNode()
                        curr = curr.char[w]
                    curr.isword=True
        t = Trie(words)
        def backtrack(i):
            if i == len(s):
                return 0
            if i in dp:
                return dp[i]
            res = backtrack(i+1)+1
            curr = t.root
            for j in range(i,len(s)):
                if s[j] not in curr.char:
                    break
                curr = curr.char[s[j]]
                if curr.isword:
                    res = min(res,backtrack(j+1))
            dp[i] = res
            return res
        return backtrack(0)
