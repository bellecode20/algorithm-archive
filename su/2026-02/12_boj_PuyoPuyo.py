# Puyo Puyo https://www.acmicpc.net/problem/11559

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

from collections import deque, defaultdict
from copy import deepcopy

board = [list(input().strip()) for _ in range(12)]

def pprint(brd):
    print("----------")
    for i in range(len(brd)):
        print(brd[i])


H, W = 12, 6
answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_bomb(sr, sc):
    global board, board_visited
    queue = deque([])
    queue.append((sr, sc))

    visited = set()
    visited.add((sr, sc))
    target = board[sr][sc]

    total = 0
    new_board = deepcopy(board)
    new_board[sr][sc] = "."
    board_visited[(sr, sc)] = True

    while queue:
        row, col = queue.popleft()
        total += 1

        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if nr < 0 or nc < 0 or nr >= 12 or nc >= 6:
                continue
            if board[nr][nc] != target:
                continue
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            queue.append((nr, nc))
            new_board[nr][nc] = "."
            board_visited[(nr, nc)] = True

    if total >= 4:
        board = new_board
        return list(visited)
    else:
        return []


def drop():
    for col in range(W):
        write = H - 1

        for row in range(H-1, -1, -1):
            if board[row][col] != ".":
                board[write][col] = board[row][col]
                write -= 1

        for row in range(write + 1):
            board[row][col] = "."
            

while True:
    bomb = []
    board_visited = defaultdict()

    for r in range(H):
        for c in range(W):
            if board[r][c] == "." or (r, c) in board_visited:
                continue
            bomb.extend(get_bomb(r, c))  # 터져야 하는 애들

    if not bomb:
        break

    drop()
    answer += 1
    
print(answer)


# 내리기 함수 버전2
def drop_ver2():
    for col in range(W):
        blocks = []

        # 아래 -> 위로 스캔해서 순서 보존
        for row in range(H - 1, -1, -1):
            if board[row][col] != ".":
                blocks.append(board[row][col])

        # 해당 컬럼 비우기
        for row in range(H):
            board[row][col] = "."

        # 아래부터 채우기
        for i, block in enumerate(blocks):  # 인덱스와 값
            board[H - 1 - i][col] = block