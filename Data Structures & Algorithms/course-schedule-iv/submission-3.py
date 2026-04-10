class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        l_prereq = defaultdict(set)

        for x,y in prerequisites:
            adj[x].append(y)
        
        def dfs(x):
            if x not in l_prereq:
                l_prereq[x].add(x)
                for a in adj[x]:
                    b = dfs(a)
                    l_prereq[a] = b
                    l_prereq[x] = l_prereq[x].union(b)
            return l_prereq[x]
        print(l_prereq)
        for i in range(numCourses):
            dfs(i)
        res = []
        for x,y in queries:
            res.append(y in l_prereq[x])
        return res
