class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #dort
        #dfs
        #remove adjacent
        #add adjacent back
        tickets.sort()
        adj = defaultdict(list)
        for o,d in tickets:
            adj[o].append(d)
        print(adj)
        res = ["JFK"]
        def dfs(port):
            if len(res) == len(tickets)+1:
                return True
            if port not in adj:
                return False
            for i in range(len(adj[port])):
                next_port = adj[port][i]
                res.append(next_port)
                adj[port].pop(i)
                print('before',adj)
                if dfs(next_port):
                    return res
                res.pop()
                adj[port].insert(i,next_port)
                print('after',adj)
            return False
        return dfs("JFK")