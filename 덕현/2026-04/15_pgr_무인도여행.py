'''
프로그래머스 무인도 여행

입력:
maps

구조:
전체 칸 돌고 bfs
섬 하나 합 구해서 answer에 넣기
끝나면 정렬 없으면 -1
'''

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = []
    for i in range(n):
        visited.append([0] * m)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    answer = []

    for r in range(n):
        for c in range(m):
            if maps[r][c] == 'X' or visited[r][c] == 1:
                continue

            q = deque()
            q.append((r, c))
            visited[r][c] = 1
            sm = int(maps[r][c])

            while q:
                cr, cc = q.popleft()

                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]

                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue
                    if visited[nr][nc] == 1:
                        continue
                    if maps[nr][nc] == 'X':
                        continue

                    visited[nr][nc] = 1
                    sm += int(maps[nr][nc])
                    q.append((nr, nc))

            answer.append(sm)

    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer