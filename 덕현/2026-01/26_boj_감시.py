'''
BOJ 15683 감시

입력:
N, M
graph

구조:
- CCTV 위치/타입 수집
- 각 CCTV 방향 경우의 수를 순서대로 적용
- 감시 표시 후 다음 CCTV 처리
- 끝까지 적용되면 사각지대 개수 최소값
'''

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# CCTV 방향(상하좌우 0123)
dir_list = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]],
    5: [[0, 1, 2, 3]],
}


def ans():
    global graph, best

    def watch(r, c, dirs):
        changed = []
        for d in dirs:
            nr = r + dr[d]
            nc = c + dc[d]
            while 0 <= nr < N and 0 <= nc < M and graph[nr][nc] != 6:
                if graph[nr][nc] == 0:
                    graph[nr][nc] = -1
                    changed.append((nr, nc))
                nr += dr[d]
                nc += dc[d]
        return changed

    def go(idx):
        global best

        if idx == len(cctvs):
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if graph[i][j] == 0:
                        cnt += 1
            if cnt < best:
                best = cnt
            return

        r, c, t = cctvs[idx]
        for dirs in dir_list[t]:
            changed = watch(r, c, dirs)
            go(idx + 1)
            for x, y in changed:
                graph[x][y] = 0

    best = 10**9
    go(0)
    return best


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            cctvs.append((i, j, graph[i][j]))

print(ans())
