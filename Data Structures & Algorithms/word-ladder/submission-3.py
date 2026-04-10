class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjacency = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" +word[j+1:] # Create all sub words
                adjacency[pattern].append(word)
        visit = set([beginWord]) # list of visited words so we dont have to do it again
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for adj in adjacency[pattern]:
                        if adj not in visit:
                            visit.add(adj)
                            q.append(adj)
            res += 1
        return 0