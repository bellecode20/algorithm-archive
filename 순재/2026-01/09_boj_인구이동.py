from collections import deque

n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(sr, sc, visited):
    q = deque()
    q.append((sr, sc))
    union = [(sr, sc)]
    visited[sr][sc] = 1
    total_pop = data[sr][sc]
    
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                diff = abs(data[cr][cc] - data[nr][nc])
                if l <= diff <= r:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    union.append((nr, nc))
                    total_pop += data[nr][nc]

    return union, total_pop

ans = 0

while True:
    visited = [[0] * n for _ in range(n)]
    move = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                union, total_pop = bfs(i, j, visited)

                if len(union) > 1:
                    move = True
                    new_pop = total_pop // len(union)
                    for ux, uy in union:
                        data[ux][uy] = new_pop

    if not move:
        break
    ans += 1

print(ans)