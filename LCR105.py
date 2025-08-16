class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        final_ans = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if visited[y][x] == 0 and grid[y][x] == 1:
                    final_ans = max(final_ans, self.bfs(visited, grid, y, x))
        return final_ans
        
    
    def bfs(self, visited, grid, cord_y, cord_x):
        ans = 0
        cur_list = [(cord_y, cord_x)]
        while cur_list:
            y, x = cur_list.pop(0)
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                if grid[y][x] == 1 and visited[y][x] == 0:
                    cur_list.append((y + 1, x))
                    cur_list.append((y - 1, x))
                    cur_list.append((y, x + 1))
                    cur_list.append((y, x - 1))
                    visited[y][x] = 1
                    ans += 1
        return ans