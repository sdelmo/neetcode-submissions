class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if ROWS == 1 and COLS == 1:
            return 1
            
        cache = {}

        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            cache[(r,c)] = dfs(r+1,c) + dfs(r,c+1)
            return cache[(r,c)]
        
        dfs(0,0)
        return cache[(0,0)]
            

