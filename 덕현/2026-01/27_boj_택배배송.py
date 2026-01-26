'''
BOJ 5972 택배 배송

입력:
N, M
graph

구조:
다익스트라?
우선순위 큐
'''

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = float("inf")

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


dist = [INF] * (N + 1)
dist[1] = 0

pq = [(0, 1)]

while pq:
    cost, x = heapq.heappop(pq)
    if cost != dist[x]:
        continue

    for nx, w in graph[x]:
        ncost = cost + w
        if ncost < dist[nx]:
            dist[nx] = ncost
            heapq.heappush(pq, (ncost, nx))

print(dist[N])
