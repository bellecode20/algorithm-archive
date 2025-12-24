from collections import deque

def d_check(r, c, mf):
    if (mf[r+1][c] == 0 and mf[r+2][c] == 0 and mf[r+1][c-1] == 0 and mf[r+1][c+1] == 0):
        return 1
    else:
        return 0

def l_check(r, c, mf): 
    if (mf[r][c-1] == 0 and mf[r+1][c-2] == 0 and mf[r+2][c-1] == 0):
        return 1
    else:
        return 0

def r_check(r, c, mf):
    if (mf[r][c+1] == 0 and mf[r+1][c+2] == 0 and mf[r+2][c+1] == 0):
        return 1
    else:
        return 0

def monster(r, c, n, mf):
    mf[r][c] = n
    mf[r][c-1] = n
    mf[r][c+1] = n
    mf[r-1][c] = n
    mf[r+1][c] = n

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

r, c, k = map(int, input().split())
respawn = [tuple(map(int, input().split())) for _ in range(k)]
data = [[0]*(c+2) for _ in range(r+4)]
ans = 0

exit_dir = [0] * k

for i in range(k):
    respawn_c, d = respawn[i]
    sr = 0
    sc = respawn_c

    exit_dir[i] = d

    while True:
        if sr + 2 >= r + 4:
            break
        if sc - 2 < 0 or sc + 2 >= c + 2:
            break

        if d_check(sr, sc, data):
            sr += 1

        elif l_check(sr, sc, data):
            sr += 1
            sc -= 1
            exit_dir[i] = (exit_dir[i] - 1) % 4

        elif r_check(sr, sc, data):
            sr += 1
            sc += 1
            exit_dir[i] = (exit_dir[i] + 1) % 4
        else:
            break

    if sr <= 1:
        data = [[0] * (c+2) for _ in range(r+4)]
        continue

    monster(sr, sc, i+1, data)

    er = sr + dr[exit_dir[i] + 1]
    ec = sc + dc[exit_dir[i] + 1]
    exit_pos = (er, ec)

    visited = [[0]*(c+2) for _ in range(r+4)]
    q = deque()

    for rr, cc in [(sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)]:
        if 0 <= rr < r+4 and 0 <= cc < c+2:
            visited[rr][cc] = 1
            q.append((rr, cc))

    mx_row = sr
    while q:
        cr, cc = q.popleft()
        mx_row = max(mx_row, cr)

        for d in range(4):
            nr = cr + dr[d+1]
            nc = cc + dc[d+1]

            if not (0 <= nr < r+4 and 0 <= nc < c+2):
                continue

            if visited[nr][nc]:
                continue

            if data[nr][nc] == i+1:
                visited[nr][nc] = 1
                q.append((nr, nc))

            elif (cr, cc) == exit_pos and data[nr][nc] != 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

    ans += mx_row

print(ans)
