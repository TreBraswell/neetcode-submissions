class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        par = [i for i in range(n)]
        rank = [0] * n
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(u1,u2):
            u1 = find(u1)
            u2 = find(u2)
            if u1 == u2:
                return False
            if rank[u1] > rank[u2]:
                par[u2] = u1
                rank[u1] += rank[u2]
            else:
                par[u1] = u2
                rank[u2] += rank[u1]
            return True
        last = None
        for u1,u2 in edges:
            if not union(u1-1,u2-1):
                last = [u1,u2]
        return last