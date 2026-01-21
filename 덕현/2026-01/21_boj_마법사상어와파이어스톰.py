'''
BOJ 20058 마법사 상어와 파이어스톰

입력:
N, Q
SZ
graph
L_list

구조:
- L마다 2^L x 2^L 단위로 전체 회전
- 회전 후, 얼음 칸 기준 상하좌우 얼음 3 미만이면 1 감소 한방에
- 모든 시전 후
  1) 얼음 총합
  2) 얼음 덩어리 최대 크기 구하기 bfs?하면될듯
'''

from collections import deque

#상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    global graph

    for L in L_list:
        s = 2 ** L

        if s != 1:
            new_graph = [[0] * SZ for _ in range(SZ)]
            for sr in range(0, SZ, s):
                for sc in range(0, SZ, s):
                    for i in range(s):
                        for j in range(s):
                            new_graph[sr + j][sc + (s - 1 - i)] = graph[sr + i][sc + j]
            graph = new_graph

        dec = []
        for r in range(SZ):
            for c in range(SZ):
                if graph[r][c] == 0:
                    continue

                cnt = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < SZ and 0 <= nc < SZ and graph[nr][nc] > 0:
                        cnt += 1

                if cnt < 3:
                    dec.append((r, c))

        for r, c in dec:
            graph[r][c] -= 1

    total = 0
    for i in range(SZ):
        total += sum(graph[i])

    visited = [[0] * SZ for _ in range(SZ)]
    best = 0

    for i in range(SZ):
        for j in range(SZ):
            if graph[i][j] == 0 or visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            cnt = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dr[k]
                    ny = y + dc[k]
                    if 0 <= nx < SZ and 0 <= ny < SZ:
                        if not visited[nx][ny] and graph[nx][ny] > 0:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            cnt += 1

            if cnt > best:
                best = cnt

    return total, best


N, Q = map(int, input().split())
SZ = 2 ** N

graph = [list(map(int, input().split())) for _ in range(SZ)]
L_list = list(map(int, input().split()))

total, biggest = bfs()

print(total)
print(biggest)
