'''
BOJ 21610 마법사 상어와 비바라기

입력 :
델타
N, M
graph
moves
clouds = (N-1,0), (N-1,1), (N-2,0), (N-2,1)

구조 :
매 명령(d, s)마다 수행:
1) 구름 이동 (격자 밖이면 반대편으로 이어짐 = % N)
2) 구름 칸에 비 내리기 (물 +1)
3) 물복사버그 비 내린 칸에서 대각선 4방향 물 있는 칸 수만큼 추가
4) 구름 생성 물 >= 2 이고, 이번 턴에 비 내린 칸이 아니면 구름 생성 + 물 -2

'''

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in moves:
    s %= N

    nxt = []
    for r, c in clouds:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        nxt.append((nr, nc))
    clouds = nxt

    visited = [[0]*N for _ in range(N)]
    for r, c in clouds:
        graph[r][c] += 1
        visited[r][c] = 1

    for r, c in clouds:
        cnt = 0
        for rr, cc in diag:
            nr = r + rr
            nc = c + cc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] > 0:
                cnt += 1
        graph[r][c] += cnt

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and not visited[i][j]:
                graph[i][j] -= 2
                new_clouds.append((i, j))
    clouds = new_clouds

print(sum(map(sum, graph)))
