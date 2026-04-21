'''
BOJ 21609 상어 중학교

입력:
N M
graph

구조:
전체 돌면서 bfs
큰거 고르면서 반복
'''

from collections import deque

def bfs(sr, sc, color):
    visited = []
    for i in range(N):
        visited.append([0] * N)

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1

    arr = []
    arr.append((sr, sc))

    rainbow = []
    cnt = 1
    rainbow_cnt = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if visited[nr][nc] == 1:
                continue
            if graph[nr][nc] == -1 or graph[nr][nc] == -2:
                continue
            if graph[nr][nc] != 0 and graph[nr][nc] != color:
                continue

            visited[nr][nc] = 1
            q.append((nr, nc))
            arr.append((nr, nc))
            cnt += 1

            if graph[nr][nc] == 0:
                rainbow_cnt += 1
                rainbow.append((nr, nc))

    if cnt < 2:
        return []

    base_r = N
    base_c = N

    for r, c in arr:
        if graph[r][c] == 0:
            continue

        if r < base_r:
            base_r = r
            base_c = c
        elif r == base_r:
            if c < base_c:
                base_c = c

    return [cnt, rainbow_cnt, base_r, base_c, arr]


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

score = 0

while 1:
    groups = []

    for r in range(N):
        for c in range(N):
            if graph[r][c] <= 0:
                continue

            g = bfs(r, c, graph[r][c])
            if g:
                groups.append(g)

    if len(groups) == 0:
        break

    groups.sort(key=lambda x: (x[0], x[1], x[2], x[3]), reverse=True)

    blocks = groups[0][4]
    size = groups[0][0]

    score += size * size

    for r, c in blocks:
        graph[r][c] = -2

    for c in range(N):
        for r in range(N - 2, -1, -1):
            if graph[r][c] == -1 or graph[r][c] == -2:
                continue

            nr = r
            while 1:
                if nr + 1 >= N:
                    break
                if graph[nr + 1][c] != -2:
                    break
                nr += 1

            if nr != r:
                graph[nr][c] = graph[r][c]
                graph[r][c] = -2

    new = []
    for i in range(N):
        new.append([0] * N)

    for r in range(N):
        for c in range(N):
            new[N - 1 - c][r] = graph[r][c]

    graph = new

    for c in range(N):
        for r in range(N - 2, -1, -1):
            if graph[r][c] == -1 or graph[r][c] == -2:
                continue

            nr = r
            while 1:
                if nr + 1 >= N:
                    break
                if graph[nr + 1][c] != -2:
                    break
                nr += 1

            if nr != r:
                graph[nr][c] = graph[r][c]
                graph[r][c] = -2

print(score)