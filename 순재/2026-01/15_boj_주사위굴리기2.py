#With GPT
from collections import deque

n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r = 0
c = 0
d = 0

dice = [1, 6, 2, 5, 4, 3]

def roll(dir):
    global dice
    t, b, n, s, w, e = dice
    if dir == 0:
        dice = [w, e, n, s, b, t]
    elif dir == 2:
        dice = [e, w, n, s, t, b]
    elif dir == 1:
        dice = [n, s, b, t, w, e]
    else:
        dice = [s, n, t, b, w, e]

def score(sr, sc):
    v = data[sr][sc]
    visited = [[0]*m for _ in range(n)]
    q = deque([(sr, sc)])
    visited[sr][sc] = 1
    cnt = 1

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if data[nr][nc] == v:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    cnt += 1
    return cnt * v

ans = 0

for _ in range(k):
    nr = r + dr[d]
    nc = c + dc[d]

    if not (0 <= nr < n and 0 <= nc < m):
        d = (d+2) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    r, c = nr, nc
    roll(d)

    ans += score(r, c)

    a = dice[1]
    b = data[r][c]

    if a > b:
        d = (d+1) % 4
    elif a < b:
        d = (d+3) % 4

print(ans)