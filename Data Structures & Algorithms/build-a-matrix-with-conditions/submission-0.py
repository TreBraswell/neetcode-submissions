class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src,visit,path,adj,res):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for a in adj[src]:
                if not dfs(a,visit,path,adj,res):
                    return False
            path.remove(src)
            res.append(src)
            return True
        def top_sort(l):
            adj = defaultdict(list)
            for a,e in l:
                adj[a].append(e)
            res = []
            path = set()
            visit = set()
            for i in range(1,k+1):
                if i not in visit:
                    if not dfs(i,visit,path,adj,res):
                        return []
            return res[::-1]
        r_c = top_sort(rowConditions)
        c_c = top_sort(colConditions)
        r_c_h = {}
        c_c_h = {}
        if r_c ==[] or c_c == []:
            return [] 
        for i,v in enumerate(r_c):
            r_c_h[v] = i

        for i,v in enumerate(c_c):
            c_c_h[v] = i
        res =[ k*[0] for r in range(k)]
        for i in range(1,k+1):
            r = r_c_h[i]
            c = c_c_h[i]
            res[r][c] = i
        return res

