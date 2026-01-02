'''
델타 한 방향이 끝까지 간다는 개념
'''
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(x, y, d):
    cnt = 0
    while True:
        nx = x + dr[d]
        ny = y + dc[d]
        if graph[nx][ny] == '#':
            break
        x, y = nx, ny
        cnt += 1
        if graph[x][y] == 'O':
            return x, y, cnt, True
    return x, y, cnt, False

def bfs():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                red_pos = (i, j)
                graph[i][j] = '.'
            elif graph[i][j] == 'B':
                blue_pos = (i, j)
                graph[i][j] = '.'

    rx, ry = red_pos
    bx, by = blue_pos

    visited = set()
    visited.add((rx, ry, bx, by))

    q = deque()
    q.append((rx, ry, bx, by, 0))

    while q:
        crx, cry, cbx, cby, depth = q.popleft()

        if depth == 10:
            continue

        for d in range(4):
            if d == 0:
                first_red = crx < cbx
            elif d == 1:
                first_red = crx > cbx
            elif d == 2:
                first_red = cry < cby
            else:
                first_red = cry > cby

            if first_red:
                nrx, nry, rcnt, r_hole = move(crx, cry, d)
                nbx, nby, bcnt, b_hole = move(cbx, cby, d)
            else:
                nbx, nby, bcnt, b_hole = move(cbx, cby, d)
                nrx, nry, rcnt, r_hole = move(crx, cry, d)

            if b_hole:
                continue
            if r_hole:
                return depth + 1

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dr[d]
                    nry -= dc[d]
                else:
                    nbx -= dr[d]
                    nby -= dc[d]

            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

print(bfs())
