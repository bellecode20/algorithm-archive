"""
BOJ 14891 톱니바퀴 (시뮬레이션)

핵심:
- 회전 "여부/방향"을 먼저 전부 결정한 다음에
- 그 다음 실제로 한 번에 회전 적용해야 함 (중간에 회전시키면 비교가 꼬임)

맞닿는 인덱스:
- i번 톱니 오른쪽 = 2
- i+1번 톱니 왼쪽 = 6
"""
from collections import deque

def rotate(g, d):
    g.rotate(d)

gears = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    idx, d = map(int, input().split())
    idx -= 1

    turn = [0] * 4
    turn[idx] = d

    for i in range(idx - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:
            turn[i] = -turn[i + 1]
        else:
            break

    for i in range(idx + 1, 4):
        if gears[i - 1][2] != gears[i][6]:
            turn[i] = -turn[i - 1]
        else:
            break

    for i in range(4):
        if turn[i]:
            rotate(gears[i], turn[i])

ans = 0
for i in range(4):
    if gears[i][0]:
        ans += 1 << i

print(ans)
