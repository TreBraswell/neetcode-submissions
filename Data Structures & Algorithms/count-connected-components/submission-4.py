class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [0] * n
        par = [i for i in range(n)]
        print(par)
        def find(n):
            node = n
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node
        def union(a,b):
            a = find(a)
            b = find(b)
            if a == b:
                return 0
            if rank[a] > rank[b]:
                par[b] = a
                rank[a] +=1
            else:
                par[a] = b
                rank[b] +=1
            return 1
        res = n
        for e1,e2 in edges:
            if union(e1,e2) == 1:
                res -=1
        return res
            