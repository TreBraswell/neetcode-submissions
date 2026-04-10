class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        c = self.root
        for w in word:
            if w not in c.children:
                c.children[w] = TrieNode()
            c = c.children[w]
        c.endOfWord = True

    def search(self, word: str) -> bool:
        c = self.root
        for w in word:
            if w not in c.children:
                return False
            c = c.children[w]
        return c.endOfWord

    def startsWith(self, prefix: str) -> bool:
        c = self.root
        for w in prefix:
            if w not in c.children:
                return False
            c = c.children[w]
        return True
        