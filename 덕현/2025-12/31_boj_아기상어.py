'''
boj 16236 아기상어

1) BFS로 먹을 수 있는 물고기 후보 찾기
2) 거리 최소 -> 위(행) -> 왼(열) 우선으로 1마리 선택
3) 이동/섭취, 시간 누적
4) eat == size 이면 size 증가
먹을 수 있는 물고기 없으면 종료


입력 :
델타
N
graph

'''

from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def find_target(graph, x, y, size):
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    fishes = []

    while q:
        cx, cy = q.popleft()

        for k in range(4):
            nx = cx + dr[k]
            ny = cy + dc[k]

            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    dist[nx][ny] = dist[cx][cy] + 1
                    q.append((nx, ny))

                    if 0 < graph[nx][ny] < size:
                        fishes.append((nx, ny, dist[nx][ny]))

    if not fishes:
        return None

    fishes.sort(key=lambda x: (x[2], x[0], x[1]))  # (거리, 행, 열)
    return fishes[0]  # (nx, ny, dist)

def simulate(board, x, y):
    size = 2
    eat = 0
    time = 0

    while True:
        res = find_target(graph, x, y, size)
        if res is None:
            break

        nx, ny, d = res
        time += d

        graph[nx][ny] = 0
        x, y = nx, ny
        eat += 1

        if eat == size:
            size += 1
            eat = 0

    return time

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

ans = simulate(graph, x, y)
print(ans)