class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visited = set()
        seen = set()
        path = []

        for c,p in prerequisites:
            adj[c].append(p)
        
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)

            
            for c in adj[course]:
                if not dfs(c):
                    return False
            if course not in seen:
                path.append(course)
            seen.add(course)
            visited.remove(course)
            return True
        for n in range(numCourses):
            if n not in seen and not dfs(n):
                return []
        return path

