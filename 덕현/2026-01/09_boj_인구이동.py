'''
BOJ 16234 인구 이동

입력 :
N, L, R
graph

규칙 :
- 인접(상하좌우) 나라 인구 차이가 L 이상 R 이하 → 국경 open
- open된 나라들끼리 하나의 연합
- 연합 인구 = (총합 // 칸 수)

구조 :
while True:
    visited 초기화
    하루 동안 모든 칸 탐색
        아직 방문 안 했으면 BFS로 연합 찾기
        연합 크기 >= 2 → 인구 갱신
    인구 이동 없으면 종료
    있으면 day += 1
'''

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

day = 0

while True:
    visited = [[0]*N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            q = deque()
            q.append((i, j))
            visited[i][j] = 1

            union = [(i, j)]
            total = graph[i][j]

            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        diff = abs(graph[r][c] - graph[nr][nc])
                        if L <= diff <= R:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                            union.append((nr, nc))
                            total += graph[nr][nc]

            if len(union) > 1:
                moved = True
                avg = total // len(union)
                for r, c in union:
                    graph[r][c] = avg

    if not moved:
        break

    day += 1

print(day)
