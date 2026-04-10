class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        c = self
        for w in word:
            if w not in c.children:
                c.children[w] = TrieNode()
            c = c.children[w]
        c.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        rows,cols = len(board),len(board[0])
        res,visit = set(),set()
        def dfs(r,c,node,word):
            if r not in range(0,rows) or c not in range(0,cols) or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r - 1,c, node,word)
            dfs(r,c+1,node,word)
            dfs(r,c -1, node,word)
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)