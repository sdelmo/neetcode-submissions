class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # Dimensions are n x n
        N = len(grid)

        # Traverse 8-directionally
        dirs = [
            (1,0),
            (1,1),
            (1,-1),
            (-1,0),
            (-1,1),
            (-1,-1),
            (0,1),
            (0,-1)
        ]

        # Set root for BFS
        q = deque() # Store r,c,dist in the node
        q.append((0,0,1))
        visited = set() # So we don't revisit nodes
        while q:
            r,c, dist = q.popleft()
            # Tag node as visited
            visited.add((r,c))
            # Check if we've reached the goal
            if (r,c) == (N-1,N-1):
                return dist

            # Try traversing through neighbours
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # validate indices and check for no wall in path
                if (nr,nc) not in visited and 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    q.append((nr,nc,dist+1))
        return -1




            
