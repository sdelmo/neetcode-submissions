class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # Edge case: cannot traverse at all due to invalid input or blocked path
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        N = len(grid) #nxn matrix
        visited = set()
        q = collections.deque()
        # enqueue the root, with a distance
        q.append((0,0,1))

        # Directions we can move in
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
        # sanity check
        assert len(dirs) == 8

        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                visited.add((r,c))
                if r == N-1 and c == N-1:
                    return dist

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    # check that index is valid
                    if 0 <= nr < N and 0 <= nc < N and (nr,nc) not in visited and grid[nr][nc] != 1:
                        q.append((nr,nc,dist+1))
        return -1




                




        

        