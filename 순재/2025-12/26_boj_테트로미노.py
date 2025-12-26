def dfs(r, c, dep, tot):
    global ans
    if dep == 4:
        ans = max(ans, tot)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc, dep + 1, tot + data[nr][nc])
            visited[nr][nc] = 0

def T(r, c):
    global ans
    for skip in range(4):
        tot = data[r][c]
        check = 1
        for d in range(4):
            if d == skip:
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < n and 0 <= nc < m):
                check = 0
                break
            tot += data[nr][nc]
        if check:
            ans = max(ans, tot)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, data[i][j])
        visited[i][j] = 0
        T(i, j)

print(ans)