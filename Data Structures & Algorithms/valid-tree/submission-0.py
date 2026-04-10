class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = { i : [] for i in range(n)}
        for nm1,nm2 in edges:
            adj[nm1].append(nm2)
            adj[nm2].append(nm1)
        visited = set()
        def dfs(c,par):
            if c in visited:
                return False
            visited.add(c)
            for i in adj[c]:
                if i == par:
                    continue
                if not dfs(i,c):
                    return False
            return True
        return dfs(0,-1) and len(visited) == n