import copy
from itertools import combinations
from collections import deque

def virus_bfs(copy_data, selected_hospital):
    q = deque()
    visited = [[0] * n for _ in range(n)]
        
    for r, c in selected_hospital:
        q.append((r, c))
        visited[r][c] = 1
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n and copy_data[nr][nc] != 1 and visited[nr][nc] == 0:
                copy_data[nr][nc] = 3
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    
    time = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                if visited[i][j] == 0:
                    return -1
                time = max(time, visited[i][j] -1)
    
    return time

# 0 : 바이러스, 1 : 벽, 2 : 병원
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
hospital = []
mn = float('inf')

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            hospital.append((i, j))

for pick in combinations(hospital, m):
    copy_data = copy.deepcopy(data)
    t = virus_bfs(copy_data, pick)
    
    if t != -1:
        mn = min(mn, t)

if mn == float('inf'):
    print(-1)
else:
    print(mn)