'''
BOJ 11559 뿌요뿌요

입력:
R, C
graph

구조:
bfs로 같은 색 뭉치 찾기
4개 이상이면 터뜨릴 목록에 담기
한 번에 다 터뜨리고 중력 적용
터진 적 있으면 연쇄 +1, 없으면 끝
While 돌장
약간 그 옛날에 폭탄터트리기? 그런느낌
'''
from collections import deque

R, C = 12, 6
graph = [list(input()) for _ in range(12)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, color, visited):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    group = [(sr, sc)]

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and graph[nr][nc] == color:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    group.append((nr, nc))

    return group

def fall():
    for c in range(C):
        temp = []
        for r in range(R - 1, -1, -1):
            if graph[r][c] != '.':
                temp.append(graph[r][c])

        r = R - 1
        for x in temp:
            graph[r][c] = x
            r -= 1
        for rr in range(r, -1, -1):
            graph[rr][c] = '.'

ans = 0

while True:
    visited = [[False] * C for _ in range(R)]
    boom = []

    for r in range(R):
        for c in range(C):
            if graph[r][c] != '.' and not visited[r][c]:
                group = bfs(r, c, graph[r][c], visited)
                if len(group) >= 4:
                    boom.extend(group)

    if not boom:
        break

    for r, c in boom:
        graph[r][c] = '.'

    fall()
    ans += 1

print(ans)
