class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        def sink(r,c):
            # Validate indices, and base case, which is not land
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            # Sink cell
            grid[r][c] = "0"

            # Sink neighbours
            sink(r+1,c)
            sink(r-1,c)
            sink(r,c+1)
            sink(r,c-1)
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # Sink the island
                    sink(r,c)
                    islands += 1
        
        return islands
            