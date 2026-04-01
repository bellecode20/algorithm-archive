'''
BOJ 13460 구슬 탈출 2

입력:
N M = map(int(input().split))
graph

구조:
bfs
빨간 구슬, 파란 구슬 위치를 같이
한 방향으로 기울이면 끝까지
파란 구슬이 구멍에 빠지면 실패
빨간 구슬만 빠지면 성공
겹치면 더 많이 이동한 구슬 한 칸 뒤로
10번 안에 성공
'''


from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(r, c, d):
    cnt = 0

    while True:
        nr = r + dr[d]
        nc = c + dc[d]

        if graph[nr][nc] == '#':
            break

        r = nr
        c = nc
        cnt += 1

        if graph[r][c] == 'O':
            return r, c, cnt, True

    return r, c, cnt, False

def bfs():
    q = deque()
    q.append((rr, rc, br, bc, 0))

    visited = set()
    visited.add((rr, rc, br, bc))

    while q:
        cr, cc, br_r, br_c, cnt = q.popleft()

        if cnt == 10:
            continue

        for d in range(4):

            nrr, nrc, r_move, r_hole = move(cr, cc, d)
            nbr, nbc, b_move, b_hole = move(br_r, br_c, d)

            if b_hole:
                continue

            if r_hole:
                return cnt + 1

            if nrr == nbr and nrc == nbc:
                if r_move > b_move:
                    nrr -= dr[d]
                    nrc -= dc[d]
                else:
                    nbr -= dr[d]
                    nbc -= dc[d]

            state = (nrr, nrc, nbr, nbc)

            if state in visited:
                continue

            visited.add(state)
            q.append((nrr, nrc, nbr, nbc, cnt + 1))

    return -1

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

rr, rc, br, bc = 0, 0, 0, 0

for r in range(N):
    for c in range(M):
        if graph[r][c] == 'R':
            rr, rc = r, c
            graph[r][c] = '.'
        elif graph[r][c] == 'B':
            br, bc = r, c
            graph[r][c] = '.'

print(bfs())