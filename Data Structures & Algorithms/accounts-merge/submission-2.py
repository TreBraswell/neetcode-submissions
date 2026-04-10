class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [ i for i in range(len(accounts))]
        rank = [1] * len(accounts)

        def find(p1):
            if par[p1] != p1:
                par[p1] = find(par[p1])
            return par[p1]
        
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]
            return True
        
        adj = {}
        for i,a in enumerate(accounts):
            for email in a[1:]:
                if email in adj:
                    union(i,adj[email])
                else:
                    adj[email] = i
        connected = defaultdict(list)
        for email,i in adj.items():
            connected[par[i]].append(email)

        res = []
        for i,e in connected.items():
            res.append([accounts[i][0]] + sorted(e))
        return res

