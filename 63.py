class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        visited = [[0] * n for i in range(m)]
        def dfs(grid, y, x):
            if y == m - 1 and x == n - 1:
                return 1
            elif visited[y][x] != 0:
                return visited[y][x]
            else:
                ans = 0
                if y < m - 1:
                    if grid[y + 1][x] == 0:
                        temp = dfs(grid, y + 1, x)
                        visited[y+1][x] = temp
                        ans += temp
                if x < n - 1:
                    if grid[y][x + 1] == 0:
                        temp = dfs(grid, y, x + 1)
                        visited[y][x+1] = temp
                        ans += temp
                return ans
        return dfs(obstacleGrid, 0, 0)