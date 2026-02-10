'''
BOJ 13335 트럭

입력:
n, w, L
graph

구조:
큐로 풀기?
다리 위에 있는 트럭 무게 큐 넣기
While 돌면서
    매 초마다 한 칸 전진
    트럭 올릴 수 있으면 넣고, 아니면 0 넣기
    큐에 남은 무게가 0이고, 트럭도 다 올렸으면 끝
'''

from collections import deque

n, w, L = map(int, input().split())
graph = list(map(int, input().split()))

bridge = deque([0] * w)
time = 0
i = 0
cur = 0

while True:
    time += 1

    out = bridge.popleft()
    cur -= out

    if i < n and cur + graph[i] <= L:
        bridge.append(graph[i])
        cur += graph[i]
        i += 1


    else:
        bridge.append(0)

    if i == n and cur == 0:
        break

print(time)
