class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        par = [i for i in range(n)]

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(a,b):
            p1 = find(a)
            p2 = find(b)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] +=1
            return 1
        result = n
        for e,c in edges:
            if union(e,c) == 1:
                result-=1
        return result
