class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            l = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:l] == w2[:l]:
                print('hmm')
                return ''
            for j in range(l):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        res = []
        visited = {}
        def dfs(s):
            if s in visited:
                return visited[s]
            visited[s] = True
            for nei in adj[s]:
                if dfs(nei):
                    return True
            visited[s] = False
            res.append(s)
        for b in adj:
            if dfs(b):
                return ''
        res.reverse()
        return ''.join(res)
            