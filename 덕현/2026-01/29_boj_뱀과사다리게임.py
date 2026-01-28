'''
BOJ 16928 뱀과 사다리 게임

입력:
N, M
N줄: 사다리 (x, y)
M줄: 뱀   (u, v)

구조:
- 1~100 보드에서 bfs
- dist[pos] = 주사위 최소 횟수
- pos에서 1~6 이동
  - 범위 넘어가면 skip
  - 도착 칸이 사다리/뱀이면 즉시 이동(teleport)
- 처음 도착(100)하면 그 값이 정답
'''

from collections import deque

N, M = map(int, input().split())

move = [0] * 101  # move[x] != 0 이면 x -> move[x]
for _ in range(N + M):
    a, b = map(int, input().split())
    move[a] = b

dist = [-1] * 101
q = deque()

dist[1] = 0
q.append(1)

while q:
    cur = q.popleft()

    if cur == 100:
        break

    for d in range(1, 7):
        nxt = cur + d
        if nxt > 100:
            continue

        if move[nxt] != 0:
            nxt = move[nxt]

        if dist[nxt] != -1:
            continue

        dist[nxt] = dist[cur] + 1
        q.append(nxt)

print(dist[100])
