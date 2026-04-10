class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for s,p in  prerequisites:
            adj[s].append(p)
        visit = {}
        def dfs(c):
            
            if c in visit:
                print(c,visit[c])
                return visit[c]
            visit[c] = True
            for i in adj[c]:
                print(i)
                if dfs(i):
                    return True
            visit[c] = False
            return False
        for i in range(numCourses):
            if i not in visit and i in adj:
                if dfs(i):
                    return False
        # if len(visit.items()) != len(prerequisites):
        #     return False
        return True