dir = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
bug = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(m):
    d, s = map(int, input().split())
    s %= n

    move = []
    for r, c in cloud:
        nr = (r + dir[d][0] * s) % n
        nc = (c + dir[d][1] * s) % n
        move.append((nr, nc))

    visited = [[0] * n for _ in range(n)]
    for r, c in move:
        data[r][c] += 1
        visited[r][c] = 1

    for r, c in move:
        cnt = 0
        for dr, dc in bug:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and data[nr][nc] > 0:
                cnt += 1
        data[r][c] += cnt

    new_cloud = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and data[i][j] >= 2:
                data[i][j] -= 2
                new_cloud.append((i, j))

    cloud = new_cloud

ans = 0
for i in range(n):
    ans += sum(data[i])

print(ans)