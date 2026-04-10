class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        par = [i for i in range(n)]
        def find(me):
            res = me
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(a,b):
            a = find(a)
            b = find(b)
            if a == b:
                return 0
            if rank[a]> rank[b]:
                par[b] = a
                rank[a] +=1
            else:
                par[a] = b
                rank[b] +=1
            return 1
        result = n
        for e1,e2 in edges:
            if union(e1,e2) == 1:
                result-=1
        return result
