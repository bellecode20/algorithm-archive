# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 일부 테케 통과하지 못해 수정이 필요한 코드입니다.
# 상어의 위치는 계속 갱신하면서
# 물고기는 최소 거리인 물고기를 먹어야 하기 때문에 BFS로 탐색할 예정

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
        if 0 < graph[r][c] < 9:
            fish_cnt += 1
        elif graph[r][c] == 9:
            shark_pos = [r, c]
            graph[r][c] = 0  # 상어 시작 위치는 빈 칸으로 처리


def get_next_pos(shk_pos):
    global shark_size, next_pos, eaten, answer
    queue = deque()
    queue.append((shk_pos[0], shk_pos[1], 0))
    visited = [[0] * N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = 1

    next_pos = [0, 0]
    while queue:
        r, c, t = queue.popleft()
        # print(r, c, t)
        if 0 < graph[r][c] < shark_size:
            next_pos = [r, c]
            eaten += 1
            answer += t
            if eaten == shark_size:  # 같은 수의 물고기를 먹을 때마다 크기가 1증가한다.
                shark_size += 1
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
            if graph[nr][nc] > shark_size: continue  # 자기보다 크기가 크면 갈 수 없음
            if visited[nr][nc]: continue

            visited[nr][nc] = 1
            queue.append((nr, nc, t + 1))

    return next_pos

while True:
    shark_pos = get_next_pos(shark_pos)
    if fish_cnt == eaten:
        break

print(answer)
