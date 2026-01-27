# 택배 배송 https://www.acmicpc.net/problem/5972

# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

from collections import defaultdict
import heapq

# 한 정점에서 모든 정점까지의 최단 최단 경로 -> 다익스트라
N, M = map(int, input().split())  # 헛간, 길
graph = [[] for _ in range(N+1)]  # 인접행렬은 메모리 초과 -> 인접리스트로 구현
dist = [int(1e9)] * (N + 1)
answer = int(1e9)

for _ in range(M):
    ai, bi, ci = map(int, input().split())  # 헛간, 헛간, 소
    graph[ai].append((bi, ci))
    graph[bi].append((ai, ci))

hq = [(1, 0)]  # start, cost
dist[1] = 0
heapq.heapify(hq)
while hq:
    node, d = heapq.heappop(hq)

    for next_i, cost in graph[node]:
        next_cost = cost + d
        if dist[next_i] > next_cost:
            dist[next_i] = next_cost
            heapq.heappush(hq, (next_i, next_cost))

print(dist[N])
