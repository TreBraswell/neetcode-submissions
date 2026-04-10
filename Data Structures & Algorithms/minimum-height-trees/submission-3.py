class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj = defaultdict(list)
        for a,e in edges:
            adj[a].append(e)
            adj[e].append(a)
        q = []
        ll = {}
        for a,l in adj.items():
            if len(l) == 1:
                q.append(a)
            ll[a] = len(l)
        while q:
            print(q)
            if n <=2:
                return q
            for i in range(len(q)):
                t = q.pop(0)
                n-=1
                for nn in adj[t]:
                    ll[nn]-=1
                    if ll[nn] == 1:
                        q.append(nn)