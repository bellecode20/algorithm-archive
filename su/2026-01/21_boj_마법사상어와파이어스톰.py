# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 
# 백준_마법사 상어와 파이어스톰 https://www.acmicpc.net/problem/20058
N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2 ** N)]
levels = list(map(int, input().split()))
SIZE = 2 ** N
total = 0
cell_cnt = 0

from collections import deque, defaultdict
from copy import deepcopy


def rotate_90(sr, sc):
    global board, rotated, lv
    for i in range(CELL):
        for j in range(CELL):
            rotated[sr + j][sc + (CELL - i - 1)] = board[sr + i][sc + j]

def bfs(sr, sc):
    global total
    visited[(sr, sc)] = True
    queue = deque([(sr, sc)])
    temp = 1
    total += board[sr][sc]
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            next_r, next_c = cur_r + dr[i], cur_c + dc[i]
            if next_r < 0 or next_c < 0 or next_r >= SIZE or next_c >= SIZE:
                continue
            if board[next_r][next_c] <= 0:
                continue
            if visited[(next_r, next_c)]:
                continue
            visited[(next_r, next_c)] = True
            temp += 1
            total += board[next_r][next_c]
            queue.append((next_r, next_c))
    
    return temp

answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for q in range(Q):
    lv = levels[q]
    rotated = [[0] * SIZE for _ in range(SIZE)]
    CELL = 2 ** lv

    # 격자칸마다 회전하기
    if CELL != 1:
        for sr in range(0, SIZE, CELL):
            for sc in range(0, SIZE, CELL):
                rotate_90(sr, sc)
        board = rotated

    new_board = deepcopy(board)

    # 얼음 칸 확인
    for r in range(SIZE):
        for c in range(SIZE):
            cnt = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= SIZE or nc >= SIZE:
                    continue
                if board[nr][nc] > 0:
                    cnt += 1
            if cnt < 3:
                new_board[r][c] -= 1
                if new_board[r][c] < 0:
                    new_board[r][c] = 0

    board = new_board

visited = defaultdict(bool)
for r in range(SIZE):
    for c in range(SIZE):
        if not visited[(r, c)] and board[r][c] > 0:
            cell_cnt = max(bfs(r, c), cell_cnt)

print(total)
print(cell_cnt)
