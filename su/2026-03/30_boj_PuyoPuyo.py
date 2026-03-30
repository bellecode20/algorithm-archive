'''
[연쇄]
1) 터지는 그룹을 찾기
    터져야 하는 셀은 표시하기
2) 아래로 떨어트리기
    새로운 보드판 (0으로 초기화되어있음)
    옮기는데 표시되어있는거는 안옮김
[/연쇄]

'''
from collections import defaultdict, deque
from copy import deepcopy
from pprint import pprint

N = 12
M = 6
cnt = 0 
board = [list(input().strip()) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, visited, bomb_board):
    new_board = deepcopy(bomb_board)
    queue = deque([])
    queue.append((r, c))
    new_board[r][c] = 1  # 터졌음
    target = board[r][c]
    visited[(r, c)] = True
    bomb_cnt = 0

    while queue:
        row, col = queue.popleft()
        bomb_cnt += 1

        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue
            if visited[(nr, nc)] or board[nr][nc] != target:
                continue
            queue.append((nr, nc))
            new_board[nr][nc] = 1
            visited[(nr, nc)] = True
    
    return bomb_cnt, new_board

def get_initial_bomb():
    global board
    bomb_board = [[0] * M for _ in range(N)]
    bomb_cnt = 0
    visited = defaultdict(bool)
    for r in range(N-1, -1, -1):
        for c in range(M):
            if board[r][c] == "." or visited[(r, c)]:
                continue
            temp_cnt, temp_board = bfs(r, c, visited, bomb_board)

            if temp_cnt >= 4:
                bomb_board = temp_board
                bomb_cnt += 1


    return bomb_cnt, bomb_board

def drop():
    global bomb_board, board
    new_board = [["."] * M for _ in range(N)]
    row, col = N-1, 0
    new_row = N-1

    while col < M:  # 칼럼마다 내리기 작업
        temp_row = N-1    
        new_row = N-1  # 🔥 얘도 초기화 필수

        while row < N:  
            while True:  
                if temp_row == -1:  
                    break

                if board[temp_row][col] == "." or bomb_board[temp_row][col] == 1:  # 뿌요 찾을 때까지 위로 탐색
                    temp_row -= 1
                    continue

                break

            if temp_row == -1:
                col += 1  # 다음 칼럼 보기
                break

            row = temp_row
            new_board[new_row][col] = board[row][col]
            new_row -= 1
            temp_row -= 1   # 🔥 어쨌든 얘도 -1해야됨
                

    return new_board

while True:
    bomb_cnt, bomb_board = get_initial_bomb()

    if bomb_cnt == 0:
        break
    
    board = drop()
    cnt += 1

print(cnt)

