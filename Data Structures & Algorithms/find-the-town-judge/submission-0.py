class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(list)
        likes =set()
        for x,y in trust:
            likes.add(x) 
            adj[y].append(x)
        for i in range(1,n+1):
            if len(adj[i]) == n-1 and i not in likes:
                return i
        return -1
