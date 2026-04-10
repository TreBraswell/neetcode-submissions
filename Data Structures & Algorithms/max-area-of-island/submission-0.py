class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_res = 0
        def bfs(row,col):
            queue = []
            res = 0
            queue.append([row,col])
            while queue:
                r,c = queue.pop(0)
                print(r,c)
                if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] == 0:
                    continue
                visited.add((r,c))
                res += 1
                queue.append([r+1,c])
                queue.append([r-1,c])
                queue.append([r,c+1])
                queue.append([r,c-1])
            return res

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs_result = bfs(r,c)

                    max_res = max(max_res, bfs_result)
        return max_res