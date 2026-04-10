class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        obs =[[0 for c in range(COLS)] for r in range(ROWS)]
        if obstacleGrid[ROWS-1][COLS-1] == 1 or obstacleGrid[0][0] == 1:

            return 0
        obs[ROWS-1][COLS-1] =1
        print(obs)
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                if r == ROWS-1 and c== COLS-1:
                    continue
                right = 0
                if c + 1 in range(COLS) and obstacleGrid[r][c+1] != 1:
                    right = obs[r][c+1]
                down = 0
                if r + 1 in range(ROWS) and obstacleGrid[r+1][c] != 1:
                    down = obs[r+1][c]
                print(right,down)
                obs[r][c] = right +down
        return obs[0][0]
