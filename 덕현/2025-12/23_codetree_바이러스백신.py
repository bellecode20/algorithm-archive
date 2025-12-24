'''
바이러스 백신

최소 시간을 구하는 문제

입력 :
N, M = map(int,input().split())
graph = list(map(int, input().split())


구조 :
0 : 바이러스, 1 : 벽 , 2 : 병원
조합 + BFS로 풀면 될듯


'''
from itertools import combinations
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
virus_pos = []     # 바이러스 위치들
hospital_pos = []  # 병원 위치들

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            virus_pos.append((i, j))
        elif graph[i][j] == 2:
            hospital_pos.append((i, j))

def bfs(chosen_hospitals):
    dist = [[-1] * N for _ in range(N)]
    q = deque()

    for x, y in chosen_hospitals:
        dist[x][y] = 0
        q.append((x, y))

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] != 1 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    max_time = 0
    for vx, vy in virus_pos:
        if dist[vx][vy] == -1:
            return float('inf')  # 이 조합 실패
        max_time = max(max_time, dist[vx][vy])

    return max_time


for hos in combinations(hospital_pos, M):
    ans = min(ans, bfs(hos))

if ans == float('inf'):
    print(-1)
else:
    print(ans)

# print(N,M)
# print(graph[0][0])



