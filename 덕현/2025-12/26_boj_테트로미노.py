'''
boj 14500 테트로미노
일정 블록을 두어서 (회전 가능) 가장 큰 수 출력
중복으로 하는 부분에 대해서 제거해야할듯..?
회전에 대해서 어떻게 처리를 할건지? (90도로 돌렸을 때, 2가지 모양, 4가지 모양이 뜨는 경우가 있으니 따로 구분)
dfs로 풀거면 t만 처리하고 나머지는 순차
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
ans = 0

max_val = 0
for i in range(n):
    row_max = max(graph[i])
    if row_max > max_val:
        max_val = row_max

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, depth, total):
    global ans

    if total + (4 - depth) * max_val <= ans:
        return

    if depth == 4:
        if total > ans:
            ans = total
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
            visited[nx][ny] = 1
            dfs(nx, ny, depth + 1, total + graph[nx][ny])
            visited[nx][ny] = -1

def check_t_shape(x, y):
    global ans

    wings = []
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            wings.append(graph[nx][ny])

    if len(wings) < 3:
        return

    center = graph[x][y]

    if len(wings) == 3:
        total = center + wings[0] + wings[1] + wings[2]
        if total > ans:
            ans = total
    else:
        total = center + sum(wings) - min(wings)
        if total > ans:
            ans = total

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = -1

        check_t_shape(i, j)

print(ans)
