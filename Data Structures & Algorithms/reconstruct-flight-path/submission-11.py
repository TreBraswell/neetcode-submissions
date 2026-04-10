class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = ["JFK"]
        tickets.sort()
        adj = defaultdict(list)
        for s,d in tickets:
            adj[s].append(d)
        
        def dfs(s):
            if len(res) == len(tickets)+1:
                return True
            if s not in adj:
                return False
            temp = adj[s].copy()
            for i in range(len(temp)):
                ns = adj[s].pop(i)
                res.append(ns)
                if dfs(ns):
                    return True
                adj[s].insert(i,ns)
                res.pop()
            return False
        dfs('JFK')
        return res
