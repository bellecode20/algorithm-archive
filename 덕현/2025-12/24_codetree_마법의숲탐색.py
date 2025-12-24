'''
마법의숲탐색

1. 입력
델타 (북동남서)
R,C,K
c,d(출발 열, 출구 방향d)

2. 구조
    1. 숲에서 넘어가는 부분을 어떻게 처리할지?
    2. 십자칸을 이동시키는 방법에대해서? 이건 근데 델타 + for문 이용해서 처리하면 될거같긴함
    3. 회전할때 출구 이동 신경쓰기
    4. 연결된 골렘 어떻게 이동할건지? bfs?


'''

from collections import deque

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc, grid, exit, H, C):
    q = deque([(sr, sc)])
    vis = [[False] * C for _ in range(H)]
    vis[sr][sc] = True

    max_r = sr
    while q:
        r, c = q.popleft()
        if r > max_r:
            max_r = r

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if nr < 0 or nr >= H or nc < 0 or nc >= C:
                continue
            if vis[nr][nc] or grid[nr][nc] == 0:
                continue


            if grid[nr][nc] == grid[r][c]:
                vis[nr][nc] = True
                q.append((nr, nc))

            elif exit[r][c]:
                vis[nr][nc] = True
                q.append((nr, nc))

    return max_r


R, C, K = map(int, input().split())
H = R + 3

graph = [[0] * C for _ in range(H)]
exit = [[False] * C for _ in range(H)]

ans = 0
gnum = 1

for _ in range(K):
    ci, d = map(int, input().split())
    y = ci - 1
    x = 1

    while True:

        def empty(r, c):
            if c < 0 or c >= C or r >= H:
                return False
            if r < 3:
                return True
            return graph[r][c] == 0

        if empty(x + 2, y) and empty(x + 1, y - 1) and empty(x + 1, y + 1):
            x += 1
            continue

        if (empty(x + 1, y - 1) and empty(x - 1, y - 1) and empty(x, y - 2)
                and empty(x + 1, y - 2) and empty(x + 2, y - 1)):
            x += 1
            y -= 1
            d = (d + 3) % 4
            continue

        if (empty(x + 1, y + 1) and empty(x - 1, y + 1) and empty(x, y + 2)
                and empty(x + 1, y + 2) and empty(x + 2, y + 1)):
            x += 1
            y += 1
            d = (d + 1) % 4
            continue

        break

    if x < 4:
        graph = [[0] * C for _ in range(H)]
        exit = [[False] * C for _ in range(H)]
        continue

    graph[x][y] = gnum
    for k in range(4):
        graph[x + dr[k]][y + dc[k]] = gnum

    ex, ey = x + dr[d], y + dc[d]
    exit[ex][ey] = True

    max_r = bfs(x, y, graph, exit, H, C)

    ans += (max_r - 2)

    gnum += 1

print(ans)