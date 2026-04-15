'''
프로그래머스 미로 탈출

입력:
maps

구조:
S,L,E 위치 정하고
bfs로 각각 이동
못가면 -1 하고 아니면 정답
'''

from collections import deque

def bfs(sr, sc, tr, tc, maps, n, m):
    visited = []
    for i in range(n):
        visited.append([0] * m)

    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c, dist = q.popleft()

        if r == tr and c == tc:
            return dist

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if visited[nr][nc] == 1:
                continue
            if maps[nr][nc] == 'X':
                continue

            visited[nr][nc] = 1
            q.append((nr, nc, dist + 1))

    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    sr = sc = 0
    lr = lc = 0
    er = ec = 0

    for r in range(n):
        for c in range(m):
            if maps[r][c] == 'S':
                sr = r
                sc = c
            elif maps[r][c] == 'L':
                lr = r
                lc = c
            elif maps[r][c] == 'E':
                er = r
                ec = c

    a = bfs(sr, sc, lr, lc, maps, n, m)
    if a == -1:
        return -1

    b = bfs(lr, lc, er, ec, maps, n, m)
    if b == -1:
        return -1

    return a + b