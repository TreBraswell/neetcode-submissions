class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [0] * n
        par = [i for i in range(n)]
        def find(goal):
            res = goal 
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(e1,e2):
            e1 = find(e1)
            e2 = find(e2)
            if e1 == e2:
                return 0
            if rank[e1] > rank[e2]:
                par[e2] = e1
                rank[e1] +=1
            else:
                par[e1] = e2
                rank[e2] +=1
            return 1
        res = n
        for e1,e2 in edges:
            if union(e1,e2) == 1:
                res -=1
        return res
