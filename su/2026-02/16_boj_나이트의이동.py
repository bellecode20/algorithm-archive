# 4 ≤ l ≤ 300 으로 백트래킹 방식 사용시 시간초과됨, 최단거리 -> BFS

from collections import deque

T = int(input())
answer = int(1e9)

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(cur_pos, goal_pos):
    global answer
    visited = [[0] * N for _ in range(N)]
    
    queue = deque()
    queue.append((cur_pos, 0))
    visited[cur_pos[0]][cur_pos[1]] = 1
    
    while queue:
        cur_pos, depth = queue.popleft()

        if cur_pos == goal_pos:
            answer = depth
            return
        
        cr, cc = cur_pos

        for i in range(8):
            nr, nc = cr + dr[i], cc + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = 1
            queue.append(((nr, nc), depth + 1))

    return int(1e9)


def solve(N, cur_pos, goal_pos):
    global answer
    answer = int(1e9)

    if cur_pos == goal_pos:
        answer = 0
        return answer
    
    bfs(cur_pos, goal_pos)  

    return answer


for _ in range(T):
    N = int(input())
    cur_pos = tuple(map(int, input().split()))
    goal_pos = tuple(map(int, input().split()))
    
    print(solve(N, cur_pos, goal_pos))
    