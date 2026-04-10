class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

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
        self.count -=1
        return True

class Solution:

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        u = UnionFind(len(nums))
        adj = {}
        for i,n in enumerate(nums):
            f= 2
            while f*f <=n:
                # print(f,n)
                if n%f==0:
                    if f in adj:
                        u.union(i, adj[f])
                    else:
                        adj[f] = i
                    while n%f == 0:
                        n = n//f
                f+=1
            # print(f,n)
            
            if n> 1:
                if n in adj:
                    u.union(i,adj[n])
                else:
                    adj[n] = i

                
        # print(u.count)
        return u.count == 1

        