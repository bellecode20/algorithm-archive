'''
4*4 공간
한 칸: 물고기 한 마리, (번호, 방향) 번호: 1이상, 16이하, 방향: 8방향
(0 0) 물고기 먹고, 방향 가지기

번호가 작은 물고기부터 순서대로 이동
한 칸 이동. 
이동 가능: 빈 칸 / 다른 물고기 있는 칸 /
이동 불가: 상어 / 밖
원할때까지 45도 반시계 회전
없으면 이동 안함
서로 위치 바꾸기!!!

상어 이동
한 번에 여러 칸 이동
물고기 있는 칸 -> 물고기 먹고, 방향 가지기
지나가는 칸에 있는 물고기는 먹지 않는다.
이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.

상어 위치, 방향
현재 물고기들 현황판 2차원 배열 [번호]
위치, 방향 기록판 [] * 16 위치 기록하기. 죽었으면 -1, -1  <--- 메인
[[위치, 방향], [], ...]

'''

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../../input.txt", "r")
input = sys.stdin.readline


# 1. 상어 처음 위치
from collections import deque
from copy import deepcopy

answer = 0
N = 4

fish_dirc = [[-1] * 2 for _ in range(17)]
board = [[0] * N for _ in range(N)]
shark = [0, 0, 0]  # row, col, dirc
D = 2
for r in range(N):
    line = list(map(int, input().split()))
    for c in range(0, 8, 2):
        idx, dirc = line[c], line[c+1]
        board[r][c // 2] = idx  # 번호  ㅁㅊㅡㅡ
        fish_dirc[line[c]] = [r, c // 2, dirc]  # 위치, 방향  이게 아니라 위치가 있어야 된다고...

direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]  # ↑, ↖, ←, ↙,    ↓, ↘, →, ↗ 

fish_idx = board[0][0]
print(fish_idx)
shark[D] = fish_dirc[fish_idx]

fish_dirc[fish_idx] = [-1, -1, -1]  # 먹힘
board[0][0] = 0

queue = deque([])
queue.append((board, fish_dirc, shark, 1))

for i in range(4):
    print(board[i])
print(fish_dirc)

def move_fish():
    global new_board, new_fish_dirc, new_shark
    # 1~16번까지
    for i in range(1, 17):
        if new_fish_dirc[i] == [-1, -1, -1]:  # 
            continue

        cur_row, cur_col, cur_dirc = new_fish_dirc[i]
        
        for i in range(8):
            next_d = (cur_dirc - i) % 8
            nr, nc = cur_row + direction[next_d][0], cur_col + direction[next_d][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if (nr, nc) == (new_shark[0], new_shark[1]):
                continue
            
            
            new_board[nr][nc], new_board[cur_row][cur_col] = new_board[cur_row][cur_col], new_board[nr][nc]  # 보드판 swap

            if new_board[nr][nc] != 0:  # 빈 칸
                new_fish_dirc[i][0], new_fish_dirc[i][1] = next_row, next_col  # 위치 바꾸기


        # 45도 반시계

    return

# def move_shark(turn):
#     global answer, queue
#     # 방향대로 상어 이동하기
#     # if 이동 가능하면
#         queue.append()
#         return 1
    
#     # if 범위 밖이면.. <= 근데 안해도 될듯

#     # if 이동 불가시
#     return 0



while queue:
    brd, f, shk, cnt = queue.popleft()
    
    new_board, new_fish_dirc, new_shark = deepcopy(brd), deepcopy(f), deepcopy(shk)

    # 2. 물고기들 이동
    move_fish()

    break

    can_go = False
    for i in range(4):
        success, next_pos = check_and_move(i)
        if success:
            can_go = True
            new_board, new_fish, new_shark, new_cnt = move_shark(next_pos)
            queue.append((new_board, new_fish, new_shark, cnt + new_cnt))  # 다먹었으면!



# print(answer)

        # for j in range(8, -1, -):  # 현재 위치를 기준으로 돌리는 거면 이렇게 하기 힘드네
