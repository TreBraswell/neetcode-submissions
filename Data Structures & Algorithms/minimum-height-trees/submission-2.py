class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj = defaultdict(list)
        for a,e in edges:
            adj[a].append(e)
            adj[e].append(a)
        s = {}
        q = []
        for a,e in adj.items():
            if len(e) ==1:
                q.append(a)
            s[a] = len(e)
        while q:
            if n <=2:
                return q
            for i in range(len(q)):
                b = q.pop(0)
                n-=1
                for nei in adj[b]:
                    s[nei] -=1
                    if s[nei] ==1:
                        q.append(nei)

        