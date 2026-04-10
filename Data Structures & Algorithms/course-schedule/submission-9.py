class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for c,p in prerequisites:
            adj[c].append(p)
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for next_course in adj[course]:
                if not dfs(next_course):
                    return False
            visited.remove(course)
            return True
        for c,p in prerequisites:
            if not dfs(c):
            
                return False
        return True

