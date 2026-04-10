class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        for c,pre in prerequisites:
            adj[c].append(pre)
        visit = set()
        result = set()
        result_list = []
        def dfs(c):
            if c in visit:
                return False
            if c in result:
                return True
            visit.add(c)
            for i in adj[c]:
                if not dfs(i):
                    return False            
            result.add(c)
            visit.remove(c)
            result_list.append(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result_list