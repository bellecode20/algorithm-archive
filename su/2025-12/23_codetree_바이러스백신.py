from collections import deque
from itertools import combinations

# 입력 텍스트 파일 실행 코드
# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).parent
# sys.stdin = open(BASE_DIR / "input.txt", "r")
# input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = int(1e9)
virus_cnt = 0

VIRUS, WALL, HOSPITAL = 0, 1, 2
virus, hospitals = [], []

for r in range(N):
    for c in range(N):
        if graph[r][c] == VIRUS:
            virus.append((r, c))
            virus_cnt += 1
        elif graph[r][c] == HOSPITAL:
            hospitals.append((r, c, 0))

if virus_cnt == 0:  # 처음부터 바이러스가 없는 경우
    print(0)
else:
    candidates = combinations(hospitals, M)  # 가능한 모든 조합 후보들

    for hsp_list in candidates:
        visited = [[0] * N for _ in range(N)]
        queue = deque(hsp_list)

        for hr, hc, _ in hsp_list:
            visited[hr][hc] = 1

        rest_virus = virus_cnt

        max_time = 0
        while queue:
            row, col, time = queue.popleft()

            if time >= answer:
                break
            
            if rest_virus == 0:
                answer = min(answer, max_time) 
                break

            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                if graph[nr][nc] == WALL: continue
                if visited[nr][nc]: continue
                
                if graph[nr][nc] == VIRUS:
                    rest_virus -= 1
                    max_time = max(max_time, time + 1)  # 매번 최대 시간을 갱신해주어야 함
                    
                visited[nr][nc] = 1
                queue.append((nr, nc, time + 1))
            

    if answer != int(1e9):
        print(answer)
    else:
        print(-1)