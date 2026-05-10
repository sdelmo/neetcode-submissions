class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        dirs = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            # validate indices, and avoid water, return to caller
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0":
                return
            
            # At this point we know we are at a land cell
            # The idea is that we use DFS to traverse and sink the entire island

            # Sink current cell
            grid[r][c] = "0"
            # Sink its neighbours (the rest of the island)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr,nc)
        
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands



