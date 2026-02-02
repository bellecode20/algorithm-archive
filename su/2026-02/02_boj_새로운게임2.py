# https://www.acmicpc.net/problem/17837

# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline


from collections import deque, defaultdict

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]  # (0흰 1빨, 2파)
pieces = [[[] for _ in range(N)] for _ in range(N)]
dirc_info = defaultdict(int)
pos = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 오 왼 위 아


for idx in range(1, K+1):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    pieces[r][c].append(idx)
    dirc_info[idx] = d


def get_cur_pos(target):
    for r in range(N):
        for c in range(N):
            for i in range(len(pieces[r][c])):
                if pieces[r][c][i] == target:
                    return [r, c, i]
            
    return [int(1e9), int(1e9), int(1e9)]

def reverse_dirc(cur_d):
    if cur_d == 0:
        cur_d = 1
    elif cur_d == 1:
        cur_d = 0
    elif cur_d == 2:
        cur_d = 3
    elif cur_d == 3:
        cur_d = 2

    return cur_d

def is_end(row, col):
    if row < 0 or col < 0 or row >= N or col >= N:
        return False
    if len(pieces[row][col]) >= 4:
        return True
    return False


def move():
    for tc in range(1, 1001):
        for k in range(1, K+1):

            r, c, index = get_cur_pos(k)  # k번 말의 현재 위치
            d = dirc_info[k]
            # 현재 방향으로 다음 칸 탐색
            nr, nc = r + pos[d][0], c + pos[d][1]

            # 칸 밖이거나 파란색인 경우
            if (nr < 0 or nc < 0 or nr >= N or nc >= N) or board[nr][nc] == 2:

                # 현재 말의 이동 방향을 반대로 하고 한 칸 이동한다.
                nd = reverse_dirc(d)
                nr, nc = r + pos[nd][0], c + pos[nd][1]
                dirc_info[k] = nd

                if (nr < 0 or nc < 0 or nr >= N or nc >= N) or board[nr][nc] == 2:
                    continue

                
            # 공통 이동 로직
            stacked = pieces[r][c][index:]
            pieces[r][c] = pieces[r][c][:index]
            
            if board[nr][nc] == 1:
                stacked = stacked[::-1]
            
            pieces[nr][nc].extend(stacked)

            if len(pieces[nr][nc]) >= 4:
                return tc

    return -1


answer = move()
print(answer)