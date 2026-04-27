from collections import deque
from copy import deepcopy
from pprint import pprint

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    graph = deepcopy(land)
    
    queue = deque()
    idx = 1
    for row in range(n):
        for col in range(m):
            if land[row][col] == 1:
                queue.append((row, col))
                size = 1
                cell = [(row, col)]
                land[row][col] = 0

                while queue:
                    r, c = queue.popleft()
                    
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if nr < 0 or nc < 0 or nr >= n or nc >= m: continue
                        if land[nr][nc] == 0: continue
                        queue.append((nr, nc))
                        cell.append((nr, nc))
                        land[nr][nc] = 0
                        size += 1
                
                # 찾은 사이즈로 채워넣기
                for new_r, new_c in cell:
                    graph[new_r][new_c] = (size, idx)  # 사이즈만 저장하면 다른 석유인지 구별 안됨. 인덱스도 같이 저장해서 나중에 set에서 활용
                
                idx += 1


    oils = [0] * m
    for col in range(m):  
        candidate = set()  # 중복 제거
        for row in range(n):
            if graph[row][col] != 0:
                candidate.add(graph[row][col])
        
        for c in candidate:
            size, cell_idx = c
            oils[col] += size

    return max(oils)
