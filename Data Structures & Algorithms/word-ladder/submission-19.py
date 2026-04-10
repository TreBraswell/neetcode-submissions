class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        visited = set()
        for word in wordList:
            for i in range(len(word)):
                nw = word[0:i] + "*" + word[i+1:]
                print(nw)
                adj[nw].append(word)
        q = []
        q.append(beginWord)
        res =1
        while q:
            for i in range(len(q)):
                w = q.pop(0)
                if w == endWord:
                    return res
                if w not in visited:
                    visited.add(w)
                    for i in range(len(w)):
                        nw = w[0:i] + "*" + w[i+1:]
                        print('final ',nw )
                        q.extend(adj[nw])
            res+=1
        return 0