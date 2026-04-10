class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            l = min(len(w1),len(w2))
            if w1[:l] == w2[:l] and len(w1) > len(w2):
                return ""
            for i in range(l):
                if w1[i] != w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for a in adj[c]:
                if dfs(a):
                    return visit[c]
            res.append(c)
            visit[c] = False
        for a in  adj.keys():
            if dfs(a):
                return ''
        res.reverse()
        res = ''.join(res)
        return res
        
            




