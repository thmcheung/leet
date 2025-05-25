class Solution:
    # Define connections based on tile type
    direction_map = {
        1: [(0, -1), (0, 1)],        # left, right
        2: [(-1, 0), (1, 0)],        # up, down
        3: [(1, 0), (0, -1)],        # down, left
        4: [(1, 0), (0, 1)],         # down, right
        5: [(-1, 0), (0, -1)],       # up, left
        6: [(-1, 0), (0, 1)]         # up, right
    }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid:
            return False

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        while queue:
            x, y = queue.popleft()
            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in self.direction_map[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Check if next cell can connect back to current cell
                    for bdx, bdy in self.direction_map[grid[nx][ny]]:
                        if nx + bdx == x and ny + bdy == y:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            break

        return False
