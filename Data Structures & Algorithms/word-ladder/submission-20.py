class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        visit = set()
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                nw = word[0:i] + "#" + word[i+1:]
                adj[nw].append(word)
        q = []
        q.append(beginWord)
        res =1
        while q:
            for w in range(len(q)):
                word = q.pop(0)
                if word == endWord:
                    return res
                if word not in visit:
                    visit.add(word)
                    for i in range(len(word)):

                        nw = word[0:i] + "#" + word[i+1:]
                        q.extend(adj[nw])
            res+=1
        return 0