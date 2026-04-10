class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,v in enumerate(edges):
            v.append(i)
        edges.sort(key=lambda x:x[2])
        u = UnionFind(n)
        mst_weight= 0
        for a,b,w,i in edges:
            if u.union(a,b):
                mst_weight +=w
        
        crit = []
        p_crit = []
        for a,b,w,i in edges:
            weight = 0
            u = UnionFind(n)
            for aa,bb,ww,ii in edges:
                if ii == i:
                    continue
                if u.union(aa,bb):
                    weight +=ww

            if max(u.rank) != n or weight>mst_weight:
                crit.append(i)
                continue

            u = UnionFind(n)
            u.union(a,b)
            weight = w
            for aa,bb,ww,ii in edges:
                if u.union(aa,bb):
                    weight +=ww   
            if weight == mst_weight:
                p_crit.append(i)
        return [crit,p_crit]


