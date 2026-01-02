#With GPT
from collections import deque

def move(r, c, dr, dc):
    cnt = 0
    while data[r + dr][c + dc] != '#' and data[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] == 'R':
            rr, rc = i, j
            data[i][j] = '.'
        if data[i][j] == 'B':
            br, bc = i, j
            data[i][j] = '.'

for i in range(n):
    for j in range(m):
        if data[i][j] == 'O':
            hole = (i, j)

q = deque([(rr, rc, br, bc, 1)])
visited = {(rr, rc, br, bc)}
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = -1

while q:
    rx, ry, bx, by, d = q.popleft()

    if d > 10:
        break

    for dr, dc in dir:
        nrr, nrc, r_cnt = move(rx, ry, dr, dc)
        nbr, nbc, b_cnt = move(bx, by, dr, dc)

        if (nbr, nbc) == hole:
            continue

        if (nrr, nrc) == hole:
            answer = d
            q.clear()
            break

        if nrr == nbr and nrc == nbc:
            if r_cnt > b_cnt:
                nrr -= dr
                nrc -= dc
            else:
                nbr -= dr
                nbc -= dc

        state = (nrr, nrc, nbr, nbc)
        if state not in visited:
            visited.add(state)
            q.append((nrr, nrc, nbr, nbc, d + 1))

print(answer)
