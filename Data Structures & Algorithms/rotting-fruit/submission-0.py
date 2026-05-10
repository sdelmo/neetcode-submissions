class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        from collections import deque
        rottenq, fresh = deque(), 0
        ROWS, COLS = len(grid), len(grid[0])

        # Get a count of fresh fruit, so we can terminate when we have rotten all of them, or know that there is one we cant rot
        for r in range(ROWS):
            for c in range(COLS):
                fresh += 1 if grid[r][c] == 1 else 0
                # populate our queue/frontier with rotting fruit, we emanate from there
                if grid[r][c] == 2:
                    rottenq.append((r,c))
        
        # the above is a r*c operation as we have to check each node in the graph
        minutes = 0
        while rottenq and fresh > 0:
            for _ in range(len(rottenq)):
                r,c = rottenq.popleft()

                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc

                    # bound validation
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) and grid[nr][nc] == 1:
                        # rot
                        grid[nr][nc] = 2
                        fresh -= 1
                        #enqueue to rotten
                        rottenq.append((nr,nc))
            minutes += 1
        return minutes if not fresh else -1


        

        
