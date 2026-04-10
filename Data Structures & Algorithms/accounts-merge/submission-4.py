class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rank = [1] * len(accounts)
        par = [i for i in range(len(accounts))]
        def find(p1):
            if p1 != par[p1]:
                par[p1] = find(par[p1])
            return par[p1]

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            return True
        adj = {}
        for i,a in enumerate(accounts):

            for email in a[1:]:
                if email in adj: 
                    union(i,adj[email])
                else:
                    adj[email] = i
        combined = defaultdict(list)
        for e,i in adj.items():
            combined[par[i]].append(e)
        print(adj,par)
        print(combined)
        res = []
        for i,c in combined.items():
            res.append([accounts[i][0]] + sorted(c))
        return res

