class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Find an island, sink it, count,
        continue
        """

        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        def sink(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            # sink cell
            grid[r][c] = "0"

            # sink its neighbours
            for dr, dc in [
                (1, 0), # down
                (-1, 0), # up
                (0, 1), # right
                (0, -1) # left
            ]:
                nr, nc = r + dr, c + dc
                # Sink neighbours
                sink(nr,nc)
            


        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    sink(r,c)
                    islands += 1
        
        return islands

        
