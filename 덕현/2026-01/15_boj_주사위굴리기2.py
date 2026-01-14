'''
BOJ 23288 주사위 굴리기 2

입력:
N, M, K
graph

주사위:
- 위 아래 북남서동
- 시작: (0,0), 방향: 동쪽

이동 규칙:
1) 현재 방향으로 1칸 이동 (막히면 방향 반대로 바꾸고 이동)
2) 주사위 굴리기
3) 점수 획득:
   - 현재 칸 값 B
   - (현재 칸과 같은 값)으로 연결된 영역 크기 C (4방향 BFS)
   - 점수 += B * C
4) 방향 결정:
   - A = 주사위 아랫면
   - B = 현재 칸 값
   - A > B : 시계방향 90도
   - A < B : 반시계방향 90도
   - A == B : 유지

출력:
총 점수
'''

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def roll(dice, d):
    top, bottom, north, south, west, east = dice
    if d == 0:      # 동
        return (west, east, north, south, bottom, top)
    if d == 2:      # 서
        return (east, west, north, south, top, bottom)
    if d == 1:      # 남
        return (north, south, bottom, top, west, east)
    # 북
    return (south, north, top, bottom, west, east)

def bfs_score(sr, sc):
    val = graph[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    cnt = 1

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] == val:
                visited[nr][nc] = True
                q.append((nr, nc))
                cnt += 1

    return val * cnt

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

score = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            val = graph[i][j]
            q = deque([(i, j)])
            visited[i][j] = True
            cells = [(i, j)]
            cnt = 1

            while q:
                r, c = q.popleft()
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] == val:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        cells.append((nr, nc))
                        cnt += 1

            s = val * cnt
            for r, c in cells:
                score[r][c] = s

# 주사위 초기 (위 : 1, 아래 : 6, 북 : 2, 남 : 5, 서 : 4, 동 :   3
dice = (1, 6, 2, 5, 4, 3)

r = 0
c = 0
d = 0  # 동

ans = 0

for _ in range(K):
    nr = r + dr[d]
    nc = c + dc[d]

    if not (0 <= nr < N and 0 <= nc < M):
        d = (d + 2) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    r, c = nr, nc
    dice = roll(dice, d)

    ans += score[r][c]

    A = dice[1]
    B = graph[r][c]
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d + 3) % 4

print(ans)
