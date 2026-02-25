# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 다익스트라

import heapq
from collections import defaultdict

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    hq = []
    heapq.heapify(hq)
    heapq.heappush(hq, (1, 0))
    
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[1] = 0
    
    while hq:
        node, d = heapq.heappop(hq)
        for next_node in graph[node]:
            if dist[next_node] > d + 1:
                dist[next_node] = d + 1
                heapq.heappush(hq, (next_node, d + 1))
    
    max_n = max(dist[1:])
    answer = 0
    for i in range(1, n + 1):
        if dist[i] == max_n:
            answer += 1
    return answer