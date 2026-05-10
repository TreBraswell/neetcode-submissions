class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x,y in prerequisites:
            adj[y].append(x)
        visit = set()
        def dfs(n):
            if n in visit:
                return False
            visit.add(n)
            for x in adj[n]:
                if not dfs(x):
                    return False
            visit.remove(n)
            return True
        for x,y in prerequisites:
            if not dfs(y):
                return False
        return True