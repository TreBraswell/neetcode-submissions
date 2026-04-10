class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set ()
        visited = set()
        res = []
        adj = defaultdict(list)
        for s,d in prerequisites:
            adj[s].append(d)
        def dfs(n):
            if n in cycle:
                print(n)
                return False
            if n in visited: 
                return True


            cycle.add(n)
            visited.add(n)
            for neigh in adj[n]:
                if not dfs(neigh):
                    return False
            res.append(n)
            cycle.remove(n)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
