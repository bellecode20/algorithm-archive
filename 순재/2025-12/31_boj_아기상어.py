from collections import deque

n = int(input())
data = []
for i in range(n):
    row = list(map(int, input().split()))
    data.append(row)

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark_r, shark_c = i, j
            data[i][j] = 0

shark_size = 2
cnt = 0
ans = 0

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

def bfs(r, c):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True
    
    lst = []
    min_dist = None
    
    while q:
        cr, cc, dist = q.popleft()
        
        if min_dist is not None and dist > min_dist:
            break
        
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                if data[nr][nc] <= shark_size:
                    visited[nr][nc] = True
                    if 0 < data[nr][nc] < shark_size:
                        if min_dist is None:
                            min_dist = dist + 1
                        lst.append((dist+1, nr, nc))
                    q.append((nr, nc, dist+1))

    if not lst:
        return None
    lst.sort(key=lambda x: (x[0], x[1], x[2]))
    return lst[0]

while True:
    target = bfs(shark_r, shark_c)
    if target is None:
        break
    
    dist, fish_r, fish_c = target
    ans += dist
    
    shark_r, shark_c = fish_r, fish_c
    data[fish_r][fish_c] = 0

    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(ans)
