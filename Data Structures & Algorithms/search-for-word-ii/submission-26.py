class Solution:


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Node():
            def __init__(self):
                self.point = {}
                self.end_of_word = False
                self.word = ""
        visit = set()
        found_words = set()
        tree_nodes = Node()
        ROWS = len(board)
        COLS = len(board[0])
        for word in words:
            curr = tree_nodes
            for l in word:
                if not l in curr.point:
                    curr.point[l] = Node()
                curr = curr.point[l]
            curr.word = word
            curr.end_of_word = True
        def backtrack(r,c,curr):
            if curr.end_of_word:
                print("success")
                found_words.add(curr.word)
            #print(curr.point.items(),r,c)
            if not r in range(0,ROWS) or c not in range(0,COLS) or (r,c) in visit:
                #print("fails")
                return
            if not board[r][c] in curr.point:
                #print("fails")
                return
            
            visit.add((r,c))
            curr = curr.point[board[r][c]]
            backtrack(r,c+1,curr)
            backtrack(r,c-1,curr)
            backtrack(r+1,c,curr)
            backtrack(r-1,c,curr)
            visit.remove((r,c))
        for r in range(0,ROWS):
            for c in range(0,COLS):
                backtrack(r,c,tree_nodes)
        print()
        return list(found_words)


