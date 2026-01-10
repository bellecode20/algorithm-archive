# https://www.acmicpc.net/problem/16236

from pprint import pprint
from copy import deepcopy
from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
fish_cnt = 0
shark_pos, shark_size = [0, 0], 2
eaten = 0
answer = 0

for r in range(N):
    for c in range(N):
        if 1 <= graph[r][c] <= 6:
            fish_cnt += 1
        elif graph[r][c] == 9:
            shark_pos = [r, c]


def get_next_pos(shk_pos):
    global shark_size, eaten, answer
    queue = deque()
    queue.append((shk_pos[0], shk_pos[1], 0))
    visited = [[0] * N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = 1

    min_t = None
    fishes = []

    # 먹을 수 있는 물고기들 탐색
    while queue:
        r, c, t = queue.popleft()
        if min_t is not None and t > min_t:
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: 
                continue
            if graph[nr][nc] > shark_size:
                continue  # 자기보다 크기가 크면 갈 수 없음
            if visited[nr][nc]: 
                continue
            
            # 최소 거리를 초과하는 경로는 queue에 추가하지 않음
            # 이 체크가 없으면: min_t 설정 후에도
            # 더 먼 거리의 물고기가 fishes에 추가되고 queue popleft할 때 break됨
            if min_t is not None and t + 1 > min_t:
                continue

            visited[nr][nc] = 1
                
            if 0 < graph[nr][nc] < shark_size:
                if min_t is None:
                    min_t = t + 1

                fishes.append((nr, nc, t + 1))

            queue.append((nr, nc, t + 1))
    
    if not fishes:
        return None
    
    fishes.sort(key=lambda x: (x[0], x[1])) # 거리가 같은 물고기들만 있기 때문에 거리로 정렬할 필요 X
    nr, nc, d = fishes[0]

    graph[shark_pos[0]][shark_pos[1]] = 0
    graph[nr][nc] = 0

    eaten += 1
    answer += d

    if eaten == shark_size:  # 같은 수의 물고기를 먹을 때마다 크기가 1증가한다.
        shark_size += 1
        eaten = 0

    return [nr, nc]

while True:
    shark_pos = get_next_pos(shark_pos)
    if shark_pos is None:
        break

print(answer)
