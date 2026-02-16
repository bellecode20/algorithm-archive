'''
BOJ 7562 나이트의 이동

입력:
T
L

구조:
bfs돌면서 최소찾기
'''

from collections import deque

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())
for _ in range(T):
    L = int(input())

    cur_r, cur_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())

    if cur_r == goal_r and cur_c == goal_c:
        print(0)
        continue

    graph = [[-1] * L for _ in range(L)]
    q = deque()

    graph[cur_r][cur_c] = 0
    q.append((cur_r, cur_c))

    while q:
        r, c = q.popleft()

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < L and 0 <= nc < L:
                if graph[nr][nc] == -1:
                    graph[nr][nc] = graph[r][c] + 1
                    if nr == goal_r and nc == goal_c:
                        q.clear()
                        break
                    q.append((nr, nc))

    print(graph[goal_r][goal_c])
