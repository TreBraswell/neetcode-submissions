class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self,word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isEnd = True 
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        rows,cols = len(board),len(board[0])
        res = set()
        visit = set()
        for word in words:
            root.addWord(word)
        def dfs(r,c,word,node):
            if r not in range(0,rows) or c not in range(0,cols) or (r,c) in visit or board[r][c] not in node.children:
                return
            word += board[r][c]
            if word in words:
                res.add(word)
            visit.add((r,c))
            dfs(r,c+1,word,node.children[board[r][c]])
            dfs(r,c-1,word,node.children[board[r][c]])
            dfs(r+1,c,word,node.children[board[r][c]])
            dfs(r-1,c,word,node.children[board[r][c]])
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,"",root)
        return list(res)