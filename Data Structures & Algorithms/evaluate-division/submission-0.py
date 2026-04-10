class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i,v in enumerate(equations):
            x,y = v
            a = values[i]
            adj[x].append((y,a))
            adj[y].append((x,1/a))
        
        def bfs(s,t):
            if s not in adj or t not in adj:
                return -1
            q = [(s,1)]
            visit = set()
            while q:
                x,v =q.pop(0)
                if x == t:
                    return v
                visit.add(x)
                for a in adj[x]:
                    xx,vv=a
                    if xx in visit:
                        continue
                    nv = v*vv
                    q.append((xx,nv))
            return -1
        res= []
        for a,b in queries:
            res.append(bfs(a,b))
        return res