class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ar = []
        target = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    ar.append((i, j))
                if grid[i][j] == 1:
                    target += 1
        ans = 0
        while True:
            if target == 0:
                return ans
            x = len(ar)
            if x == 0:
                break
            for _ in range(x):
                i, j = ar.pop(0)
                if i + 1 < m:
                    if grid[i + 1][j] == 1:
                        grid[i + 1][j] = 2
                        ar.append((i + 1, j))
                        target -= 1
                if i - 1 >= 0:
                    if grid[i - 1][j] == 1:
                        grid[i - 1][j] = 2
                        ar.append((i - 1, j))
                        target -= 1
                if j + 1 < n: 
                    if grid[i][j + 1] == 1:
                        grid[i][j + 1] = 2
                        ar.append((i, j + 1))
                        target -= 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == 1:
                        grid[i][j - 1] = 2
                        ar.append((i, j - 1))
                        target -= 1
            ans += 1

        return -1
