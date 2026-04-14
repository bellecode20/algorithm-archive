from collections import deque
import sys

input = sys.stdin.readline

N = 4
gears = [deque(map(int, input().strip())) for _ in range(N)]
K = int(input())

for _ in range(K):
    idx, direction = map(int, input().split())
    idx -= 1

    # 각 톱니가 회전할 방향 저장
    rotate_dir = [0] * 4
    rotate_dir[idx] = direction

    # 왼쪽 전파
    for i in range(idx, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break

    # 오른쪽 전파
    for i in range(idx, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break

    # 한 번에 회전 적용
    for i in range(4):
        if rotate_dir[i] == 1:      # 시계 방향
            gears[i].appendleft(gears[i].pop())
        elif rotate_dir[i] == -1:   # 반시계 방향
            gears[i].append(gears[i].popleft())

answer = 0
score = [1, 2, 4, 8]

for i in range(4):
    if gears[i][0] == 1:
        answer += score[i]

print(answer)