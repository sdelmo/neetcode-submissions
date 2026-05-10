class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        def sinkandsize(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + sinkandsize(r+1,c) + sinkandsize(r-1,c) + sinkandsize(r,c+1) + sinkandsize(r,c-1)

        biggest = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    biggest = max(biggest, sinkandsize(r,c))
        
        return biggest
                    