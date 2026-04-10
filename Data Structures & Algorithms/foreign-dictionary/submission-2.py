class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #compare the words
        # build grapgh

        # walk grapogh and then check for over lap
        letters = set()
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            l = min(len(word1),len(word2))
            if len(word1)> len(word2) and word1[:l] == word2[:l]:
                return "" 
            for j in range(l):

                if word1[j] != word2[j]:

                    adj[word1[j]].add(word2[j])
                    break
        visited = {}
        res = []
        def dfs(cha):
            if cha in visited:
                return visited[cha]
            visited[cha] = True
            for i in adj[cha]:
                if dfs(i):
                    return True
            visited[cha] = False
            res.append(cha)
        for i in adj:
            if dfs(i):
                return ""
        res.reverse()
        res = ''.join(res)
        print(res)
        return res

            