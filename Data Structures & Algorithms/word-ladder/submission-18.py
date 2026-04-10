class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjacency = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i+1:]
                adjacency[pat].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i+1:]
                    for connection in adjacency[pat]:
                        if connection not in visit:
                            q.append(connection)
                            visit.add(connection)
            res +=1
        return 0
            