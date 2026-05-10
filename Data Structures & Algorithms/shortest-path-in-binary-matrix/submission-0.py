class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Edge case: Either an invalid matrix, or 
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        N = len(grid)

        from collections import deque
        visited = set()
        frontier = deque()
        frontier.append((0,0,1))
        dirs = [
            (1, 0),
            (1, 1),
            (1, -1),
            (-1, 0),
            (-1, 1),
            (-1, -1),
            (0, 1),
            (0, -1)
        ]

        while frontier:

            for _ in range(len(frontier)):
                r, c, dist = frontier.popleft()
                visited.add((r,c))

                # Terminate once we've reached end
                if r == N-1 and c == N-1:
                    return dist
                
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    # Check valid boundaries and traversable
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        frontier.append((nr, nc, dist + 1))
        
        return -1
                








