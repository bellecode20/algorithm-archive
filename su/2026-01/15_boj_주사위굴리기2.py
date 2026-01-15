# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 수정 중인 코드입니다.

from collections import deque, defaultdict

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) * N for _ in range(N)]

dice = [3, 4, 5, 2, 6, 1]  # 동 서 남 북 아랫면 윗면
dirc_kor = ["북", "동", "남", "서"]
dirc = 1  # 이동 방향 (0~4, 0북 1동 2남 3서)
# dirc = 0  # 이동 방향 (0~4, 0동 1서 2남 3북)
# 0 -> 3
# 1 -> 0
# 

answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
row, col = 0, 0
tc = 0

def roll(d):
    global dice
    # rolled = [0] * 6
    temp_top = dice[5]  # 윗면 임시 저장
    if d == 0:  # 북쪽
        dice[5] = dice[3]
        dice[3] = dice[4]
        dice[4] = dice[1]
        dice[1] = temp_top
    elif d == 1:  # 동쪽
        dice[5] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = temp_top
    elif d == 2:  # 남쪽
        dice[5] = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[2]
        dice[2] = temp_top
    elif d == 3:  # 서쪽
        dice[5] = dice[2]
        dice[2] = dice[4]
        dice[4] = dice[0]
        dice[0] = temp_top

def get_score(r, c, b):
    cnt = 1
    queue = deque()
    visited = defaultdict(bool)
    visited[(r, c)] = True
    queue.append((r, c))
    print()
    print(f"sr: {r}, sc: {c}")
    while queue:
        cur_r, cur_c = queue.popleft()
        print(f"cur_r: {cur_r}, cur_c: {cur_c}")
        for i in range(4):
            next_row, next_col = cur_r + dr[i], cur_c + dc[i]
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[(next_row, next_col)]:
                continue
            
            visited[(next_row, next_col)] = True
            if board[next_row][next_col] == b:
                queue.append((next_row, next_col))
                cnt += 1
    print(f"b*c: {b*cnt}")
    return b * cnt

while tc < K:
    # 이동방향 결정하기
    nr, nc = row + dr[dirc], col + dc[dirc]
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        if dirc == 0:
            dirc = 2
        elif dirc == 2:
            dirc = 0
        elif dirc == 1:
            dirc = 3
        elif dirc == 3:
            dirc = 1

    row, col = row + dr[dirc], col + dc[dirc]
    roll(dirc)  # 설정된 이동 방향으로 한 칸 굴러간다.

    A, B = dice[4], board[row][col]
    answer += get_score(row, col, B)  # 점수 획득
    
    # 이동방향 새로 결정하기
    if A > B:
        dirc = (dirc + 1) % 4
    elif A < B:
        dirc = (dirc - 1) % 4

    tc += 1
    print(dice, dirc)

print(answer)

# # 입력 텍스트 파일 실행 코드
# import sys
# from pathlib import Path
# BASE_DIR = Path(__file__).parent
# sys.stdin = open(BASE_DIR / "input.txt", "r")
# input = sys.stdin.readline

# from collections import deque, defaultdict

# N, M, K = map(int, input().split())
# board = [list(map(int, input().split())) * N for _ in range(N)]

# dice = [3, 4, 5, 2, 6, 1]  # 동 서 남 북 아랫면 윗면
# # dirc = 0  # 이동 방향 (0~4, 0북 1동 2남 3서)
# dirc = 0  # 이동 방향 (0~4, 0동 1서 2남 3북)
# # 0 -> 3
# # 1 -> 0
# # 

# answer = 0
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# row, col = 0, 0
# tc = 0

# def roll(d):
#     global dice
#     # rolled = [0] * 6
#     temp_top = dice[5]  # 윗면 임시 저장
#     if d == 0:  # 동쪽
#         dice[5] = dice[1]
#         dice[1] = dice[4]
#         dice[4] = dice[0]
#         dice[0] = temp_top
#     elif d == 1:  # 서쪽
#         dice[5] = dice[0]
#         dice[0] = dice[4]
#         dice[4] = dice[1]
#         dice[1] = temp_top
#     elif d == 2:  # 남쪽
#         dice[5] = dice[3]
#         dice[3] = dice[4]
#         dice[4] = dice[2]
#         dice[2] = temp_top
#     elif d == 3:  # 북쪽
#         dice[5] = dice[2]
#         dice[2] = dice[4]
#         dice[4] = dice[3]
#         dice[3] = temp_top

# def get_score(r, c, b):
#     c = 0
#     queue = deque()
#     visited = defaultdict(bool)
#     visited[(r, c)] = True
#     queue.append((r, c))

#     while queue:
#         cur_r, cur_c = queue.popleft()
#         for i in range(4):
#             next_row, next_col = cur_r + dr[i], cur_c + dc[i]
#             if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
#                 continue
#             if visited[(next_row, next_col)]:
#                 continue
            
#             visited[(next_row, next_col)] = True
#             if board[next_row][next_col] == b:
#                 queue.append((next_row, next_col))
#                 c += 1

#     return b * c

# while tc <= K:
#     # 이동방향 결정하기
#     nr, nc = row + dr[dirc], col + dc[dirc]
#     if nr < 0 or nc < 0 or nr >= N or nc >= M:
#         if dirc == 0:
#             dirc = 1
#         elif dirc == 1:
#             dirc = 0
#         elif dirc == 2:
#             dirc = 3
#         else:
#             dirc = 2

#     nr, nc = row + dr[dirc], col + dc[dirc]
#     roll(dirc)  # 설정된 이동 방향으로 한 칸 굴러간다.

#     A, B = dice[4], board[nr][nc]
#     answer += get_score(nr, nc, B)  # 점수 획득
    
#     # 이동방향 새로 결정하기
    
#     if A > B:
#         if dirc == 0:  # 동
        

#     # dice = roll(dirc)
#     # 아랫면에 있는
#     bottom = dice[4]
#     tc += 1

# print(answer)
