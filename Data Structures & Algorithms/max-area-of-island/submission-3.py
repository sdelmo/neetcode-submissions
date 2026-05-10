class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # Edge case: malformed input
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            # Validate boundaries and return 0 for water
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            # Sink current cell so we don't revisit
            grid[r][c] = 0

            # Sink the cells neighbours and their neighbours
            # 1 for each cell sunk, that gives us the area
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        biggest_island = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # Sink and count area
                    biggest_island = max(biggest_island, dfs(r,c))
        
        return biggest_island


        