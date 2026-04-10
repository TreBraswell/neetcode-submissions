class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        class TrieNode:
            def __init__(self):
                self.char = {}
                self.isword = False
        class Trie:
            def __init__(self,words):
                self.root = TrieNode()
                for word in words:
                    curr=  self.root 
                    for c in word:
                        if c not in curr.char:
                            curr.char[c] = TrieNode()
                        curr = curr.char[c]
                    curr.isword = True


        words = set(dictionary)
        dp = {}
        t = Trie(words)
        def back(index):
            if index ==len(s):
                return 0
            if index in dp:
                return dp[index]
            r = back(index+1)+1
            currr = t.root
            for j in range(index,len(s)):
                if s[j] not in currr.char:
                    break
                
                currr = currr.char[s[j]]
                if currr.isword:
                    r = min(r,back(j+1))
            dp[index] = r
            return r
        return back(0)