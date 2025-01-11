global word, x, y
word = input()
y = int(input())
x = int(input())
graph = [None for i in range(y)]
for i in range(y):
    graph[i] = list(map(str, input().split()))

def turn(direction_x, direction_y):
    if direction_x == 0:
        return [(1, 0), (-1, 0)]
    if direction_y == 0:
        return [(0, 1), (0, -1)]
    return [(-direction_x, direction_y), (direction_x, -direction_y)]

def dfs(graph, index, index_x, index_y, direction_x, direction_y, flag):
    cnt = 0
    first = 0  #cannot turn on first
    while True:
        proceeded = 0
        if index >= len(word) - 1:
            cnt += 1
            break

        #next cell if we continue straight
        next_x = index_x + direction_x
        next_y = index_y + direction_y
        if flag == 0 and first == 1:
            #potential new directions
            for dx_turn, dy_turn in turn(direction_x, direction_y):
                nx = index_x + dx_turn
                ny = index_y + dy_turn
                if 0 <= nx < x and 0 <= ny < y:
                    if graph[ny][nx] == word[index+1]:
                        cnt += dfs(graph, index+1, nx, ny, dx_turn, dy_turn, 1)
        if 0 <= next_x < x and 0 <= next_y < y:
            #if still in bounds, check if the next letter matches
            if graph[next_y][next_x] == word[index + 1]:
                #Move forward
                index += 1
                index_x = next_x
                index_y = next_y
                proceeded = 1
        if proceeded == 0:
            break

        first = 1
    return cnt
ans = 0
for i in range(x):
    for j in range(y):
        if graph[j][i] == word[0]:
            ans += dfs(graph, 0, i, j, 1, 1, 0)
            ans += dfs(graph, 0, i, j, 1, 0, 0)
            ans += dfs(graph, 0, i, j, 1, -1, 0)
            ans += dfs(graph, 0, i, j, 0, 1, 0)
            ans += dfs(graph, 0, i, j, 0, -1, 0)
            ans += dfs(graph, 0, i, j, -1, 1, 0)
            ans += dfs(graph, 0, i, j, -1, 0, 0)
            ans += dfs(graph, 0, i, j, -1, -1, 0)
                
print(ans)