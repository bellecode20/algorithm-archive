'''
dfs로 풀었지만
bfs가 더 적합
'''

import sys
sys.setrecursionlimit(10**6)

def solution(board):
    n = len(board)
    INF = int(1e9)
    answer = INF

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # best[r][c][dir] = (r,c)에 dir 방향으로 도착했을 때 최소 비용
    best = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    def dfs(r, c, dirc, cost):
        nonlocal answer

        if cost >= answer:
            return

        if (r, c) == (n - 1, n - 1):
            answer = min(answer, cost)
            return

        for nd in range(4):
            nr = r + dr[nd]
            nc = c + dc[nd]

            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if board[nr][nc] == 1:
                continue

            ncost = cost + 100
            if nd != dirc:
                ncost += 500

            if best[nr][nc][nd] <= ncost:
                continue

            best[nr][nc][nd] = ncost
            dfs(nr, nc, nd, ncost)

    # 시작점에서 오른쪽, 아래쪽 두 방향 출발
    if n > 1 and board[0][1] == 0:
        best[0][1][1] = 100
        dfs(0, 1, 1, 100)

    if n > 1 and board[1][0] == 0:
        best[1][0][2] = 100
        dfs(1, 0, 2, 100)

    return answer