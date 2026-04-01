`'''
BOJ 11559 뿌요뿌요

입력:
R, C
graph
델타

구조:
bfs로 같은 색 그룹 찾기
4개 이상이면 바로 터질 위치 저장
전체 탐색 끝나면 한 번에 터뜨리기
열마다 아래에서부터 다시 채워서 중력 처리
더 이상 안 터질 때까지 반복
'''
from collections import deque

R, C = 12, 6
graph = [list(input()) for _ in range(R)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, visited):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1


    color = graph[sr][sc]
    arr = []
    arr.append((sr, sc))


    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < R and 0 <= nc < C:
                if visited[nr][nc] == 0 and graph[nr][nc] == color:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    arr.append((nr, nc))
    return arr

def down():
    for c in range(C):
        idx = R - 1

        for r in range(R - 1, -1, -1):
            if graph[r][c] != '.':
                graph[idx][c] = graph[r][c]
                idx -= 1

        for r in range(idx, -1, -1):
            graph[r][c] = '.'

ans = 0

while True:
    visited = [[0] * C for _ in range(R)]
    boom = []

    for r in range(R):
        for c in range(C):
            if graph[r][c] == '.':
                continue
            if visited[r][c] == 1:
                continue

            arr = bfs(r, c, visited)

            if len(arr) >= 4:
                for i in range(len(arr)):
                    boom.append(arr[i])

    if len(boom) == 0:
        break

    for i in range(len(boom)):
        r, c = boom[i]
        graph[r][c] = '.'

    down()
    ans += 1

print(ans)`