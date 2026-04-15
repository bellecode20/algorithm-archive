from collections import deque, defaultdict

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    def bfs(sr, sc):
        nonlocal visited, maps
        queue = deque([(i, j)])
        visited[i][j] = 1
        result = int(maps[i][j])
        
        while queue:
            row, col = queue.popleft()
            for k in range(4):
                nr = dr[k] + row
                nc = dc[k] + col
                if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc]:
                    continue
                if maps[nr][nc] == "X":
                    continue
                visited[nr][nc] = 1
                result += int(maps[nr][nc])
                queue.append((nr, nc))
                
        return result 
    
    answer_list = []
    for i in range(N):
        for j in range(M):
            if visited[i][j] or maps[i][j] == "X":
                continue
            answer_list.append(bfs(i, j))
            
    if not answer_list:
        return [-1]
    
    return sorted(answer_list)