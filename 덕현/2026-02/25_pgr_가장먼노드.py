'''
프로그래머스 49189 가장 먼 노드

입력:
n
edge
graph

구조:
인접리스트 or 행렬 그래프 만들기
1번에서 bfs
젤 큰 거리 값이 몇 개인지 세기
'''

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)
    q = deque()

    dist[1] = 0
    q.append(1)

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    mx = 0
    for i in range(1, n + 1):
        if dist[i] > mx:
            mx = dist[i]

    cnt = 0
    for i in range(1, n + 1):
        if dist[i] == mx:
            cnt += 1

    return cnt