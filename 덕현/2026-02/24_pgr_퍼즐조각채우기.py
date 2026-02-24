'''
프로그래머스 84021 퍼즐 조각 채우기

구조:
- game_board에서 0덩어리 뽑기
- table에서 1덩어리 뽑기
- 모양은 좌표를 rㅣ준으로 정규화해서 비교
- 조각은 4번 회전한 모양을 만들어두고, 빈칸이랑 맞으면 채우기
'''

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(grid, sr, sc, val, visited):
    n = len(grid)
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    cells = [(sr, sc)]

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and grid[nr][nc] == val:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cells.append((nr, nc))

    return cells

def normalize(cells):
    min_r = 10**9
    min_c = 10**9
    for r, c in cells:
        if r < min_r: min_r = r
        if c < min_c: min_c = c

    temp = []
    for r, c in cells:
        temp.append((r - min_r, c - min_c))

    temp.sort()
    return temp

def rotate(shape):
    temp = []
    for r, c in shape:
        temp.append((c, -r))
    return normalize(temp)

def get_shapes(grid, val):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    shapes = []

    for r in range(n):
        for c in range(n):
            if grid[r][c] == val and not visited[r][c]:
                cells = bfs(grid, r, c, val, visited)
                shapes.append(normalize(cells))

    return shapes

def solution(game_board, table):
    holes = get_shapes(game_board, 0)
    pieces = get_shapes(table, 1)

    rot_pieces = []
    for p in pieces:
        r0 = p
        r1 = rotate(r0)
        r2 = rotate(r1)
        r3 = rotate(r2)
        rot_pieces.append([r0, r1, r2, r3])

    used = [False] * len(pieces)
    ans = 0

    for hole in holes:
        size = len(hole)
        ok = False

        for i in range(len(rot_pieces)):
            if used[i]:
                continue
            if len(rot_pieces[i][0]) != size:
                continue

            for rp in rot_pieces[i]:
                if rp == hole:
                    used[i] = True
                    ans += size
                    ok = True
                    break

            if ok:
                break

    return ans