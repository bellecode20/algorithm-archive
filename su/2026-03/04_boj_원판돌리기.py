import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline


# 반지름이 1, 2, ..., N인 원판
# 크기가 작아지는 순...
# 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다.
# (i, j): i번째 원판에 적힌 j번째 수의 위치
# 

# 총 T번 회전시키려고 한다.
# 원판의 회전 방법은 미리 정해져 있고,
# i번째 회전할 때 사용하는 변수는 xi, di, ki 이다.
# 1. 번호가 xi의 배수인 원판을! di방향으로 ki 칸 회전시킨다. (di가 0이면 시계 방향, 1인 경우는 반시계방향이다.)
# 2. 원판에 수가 남아있으면, 인접하면서 수가 같은 것들을 모두 찾는다.
    # 1) 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다. (0으로 만들자)
    # 2) 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
# 되게 어려워보인다고 생각했는데 자세히 보니깐 또 할만 할듯!

# [3, 1, 1, 2]
# [5, 2, 4, 2]
# [3, 1, 3, 5]

from collections import deque

N, M, T = map(int, input().split())  # 원판 개수, 원판에 적힌 정수 개수, 회전 횟수
disk = []
# dirc = []

def pprint(grp):
    for i in range(len(grp)):
        print(grp[i])

for i in range(N + 1):
    if i == 0:
        disk.append([-1] * M)  # 1기반 인덱스라서, 0번째는 임시 값 추가
        continue

    line = list(map(int, input().split()))
    disk.append(line)

def bfs(row, col, visited):
    visited[row][col] = 1
    queue = deque([row, col, 1])

    while queue:
        r, c, cnt = queue.popleft()
        for dd in range(4):
            pass

def get_next_num_disk(disk):
    # 인접하면서 같은 수.. 찾기
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visited = [[0] * (N + 1) for _ in range(N + 1)]

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if not visited[row][col]:
                bfs(row, col)

    return

for t in range(T):  # 회전
    x, d, k = map(int, input().split())  # 번호가 x의 배수인 원판을 d방향으로 k칸 회전시킨다. (d가 0이면 시계 방향, 1인 경우는 반시계방향이다.)
    # 1. 회전할 원판들
    candidates = []
    # break
    for i in range(1, N + 1):
        if i % x != 0:  # 배수아니면 넘기기  # 에리토 어쩌고?해야되나
            continue
        
        # 2. 회전하기 ⭐️ ㅠㅠ
        for _ in range(k):  # k칸 회전
            temp = disk[i][0]  # swipe 하기 전 값 저장
            for j in range(M):
                print("-------회전")
                print(disk[i])
                if d == 0:  # 시계방향
                    # disk[i].rotate()
                    disk[i] = disk[i][M-1:M] + disk[i][0:M-1]  # ⭐️
                else:
                    disk[i] = disk[i][1:M-1] + disk[i][:1]
                
                print(disk[i])
        
        # 원판에 수가 남아있으면
        disk = get_next_num_disk(disk)
            


pprint(disk)
# print(disk[0])
# disk[1] = disk[1][3:4] + [100]  # 
# disk[1] = disk[1][3:4] + disk[1][0:3]  # 

# disk[1].rotate()
print(disk[1])
# print(disk[1][1:4])
# print(disk[1][3:4])