class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = { i :[] for i in range(numCourses)} 
        for course, prereq in prerequisites:
            pre[course].append(prereq)
        visited = set()
        num_courses = 0
        def dfs(c):
            print(c)
            if c in visited:
                return False
            if len(pre[c]) == 0:
                return True
            # num_courses += 1
            visited.add(c)
            for i in pre[c]:
                if not dfs(i):
                    return False
            pre[c] = []
            visited.remove(c)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




