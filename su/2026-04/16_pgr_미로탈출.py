from collections import deque

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    sr = sc = er = ec = lr = lc = 0
    INF = int(1e9)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    def bfs(r, c, goal_r, goal_c):
        queue = deque([])
        queue.append((r, c, 0))
        visited = [[0] * M for _ in range(N)]
        visited[r][c] = 1
        
        while queue:
            row, col, t = queue.popleft()
            if (row, col) == (goal_r, goal_c):
                return t
            
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if nr < 0 or nc < 0  or nr >= N or nc >= M or visited[nr][nc]:
                    continue
                if maps[nr][nc] != "X":
                    visited[nr][nc] = 1
                    queue.append((nr, nc, t + 1))
        return INF
    
    for r in range(N):
        for c in range(M):
            if maps[r][c] == "S":
                sr, sc = r, c
            elif maps[r][c] == "E":
                er, ec = r, c
            elif maps[r][c] == "L":
                lr, lc = r, c

    result_1 = bfs(sr, sc, lr, lc)
    if result_1 == INF:
        return -1
    result_2 = bfs(lr, lc, er, ec)
    if result_2 == INF:
        return -1
    
    return result_1 + result_2