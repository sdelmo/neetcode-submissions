class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                fresh += 1 if grid[r][c] == 1 else 0
                if grid[r][c] == 2:
                    q.append((r,c))

        elapsed = 0

        dirs = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        # rot that thang
                        grid[nr][nc] = 2
                        fresh -= 1
                        # queue that thang
                        q.append((nr,nc))
            elapsed += 1
        
        return elapsed if not fresh else -1



