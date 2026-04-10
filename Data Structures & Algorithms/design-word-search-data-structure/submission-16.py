class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        c = self.root
        for w in word:
            if w not in c.children:
                c.children[w] = TrieNode()
            c = c.children[w]    
        c.isEndOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            c = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for refs in c.children.values():
                        if dfs(i+1,refs):
                            return True
                    return False
                else:
                    if word[i] not in c.children:
                        return False
                    c = c.children[word[i]]

            return c.isEndOfWord
        return dfs(0,self.root)
