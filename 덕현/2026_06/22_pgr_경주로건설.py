'''
프로그래머스 67259 경주로 건설

입력:
board

구조:
bfs? 100이랑 코너는 500? 600?
'''

from collections import deque


def solution(board):
    n = len(board)
    visited = []

    for d in range(4):

        temp = []

        for r in range(n):
            temp.append([float('inf')] * n)

        visited.append(temp)

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    q = deque()

    for d in range(4):
        visited[d][0][0] = 0

    q.append((0, 0, -1, 0))

    while q:

        r, c, dir, cost = q.popleft()

        for nd in range(4):

            nr = r + dr[nd]
            nc = c + dc[nd]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            if board[nr][nc] == 1:
                continue

            if dir == -1:
                new_cost = cost + 100

            else:

                if dir == nd:
                    new_cost = cost + 100

                else:
                    new_cost = cost + 600

            if visited[nd][nr][nc] > new_cost:
                visited[nd][nr][nc] = new_cost
                q.append((nr, nc, nd, new_cost))

    answer = float('inf')

    for d in range(4):

        if visited[d][n - 1][n - 1] < answer:
            answer = visited[d][n - 1][n - 1]

    return answer