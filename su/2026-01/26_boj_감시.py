# 감시 https://www.acmicpc.net/problem/15683

from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cctv_pos = []  # cctv 좌표
c_len = 0
answer = int(1e9)
rotated = []

cctv = {
    1: [(0, 1)],
    2: [(0, -1), (0, 1)],
    3: [(-1, 0), (0, 1)],
    4: [(0, -1), (-1, 0), (0, 1)],
    5: [(0, -1), (-1, 0), (0, 1), (1, 0)]
}

for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctv_pos.append((i, j))
            c_len += 1

def rotate_cctv(cctv_idx, turn):
    directions = cctv[cctv_idx][:]  # [warn]: 깊은 복사 해서 원본 direction을 바꾸지 않도록 해야 함.
    for _ in range(turn):
        for j in range(len(directions)):
            directions[j] = (directions[j][1], -directions[j][0])  # 90도 회전

    return directions

def is_in_outside(r, c):
    if r < 0 or c < 0 or r >= N or c >= M:
        return True
    return False

def run_cctv(bd, directions, sr, sc):
    new_bd = deepcopy(bd)
    for t in range(len(directions)):
        r, c = sr, sc  # [warn]: 4방향으로 뻗어나가기 전에 시작점 위치 저장해야 함. while문에서 바꿔버리면 시작점 위치 계속 변경됨
        while True:
            nr, nc = r + directions[t][0], c + directions[t][1]
            
            if is_in_outside(nr, nc) or new_bd[nr][nc] == 6:
                break
            if new_bd[nr][nc] == "#" or 1 <= new_bd[nr][nc] <= 5:
                r, c = nr, nc  # [warn]: 이어서 탐색할 때도 현재 위치를 갱신해야 함
                continue

            r, c = nr, nc 
            new_bd[r][c] = "#"
            
    return new_bd


def calc(bd):
    result = 0
    for row in range(N):
        for col in range(M):
            if bd[row][col] == 0:  
                result += 1
    return result


def dfs(depth, cur_board):
    global answer
    if depth == c_len:
        answer = min(answer, calc(cur_board))
        return
    
    (sr, sc) = cctv_pos[depth]

    if cur_board[sr][sc] == 2:
        for dirc in range(2):
            cur_directions = rotate_cctv(cur_board[sr][sc], dirc)  # 90도 회전시킨 방향..
            next_board = run_cctv(cur_board, cur_directions, sr, sc)
            dfs(depth + 1, next_board)
    elif cur_board[sr][sc] == 5:
        cur_directions = cctv[cur_board[sr][sc]]  # 회전 안 함
        next_board = run_cctv(cur_board, cur_directions, sr, sc)
        dfs(depth + 1, next_board)  # 
    else:
        for dirc in range(4):
            cur_directions = rotate_cctv(cur_board[sr][sc], dirc)  # 90도 회전시킨 방향..
            next_board = run_cctv(cur_board, cur_directions, sr, sc)
            dfs(depth + 1, next_board)


dfs(0, board)

print(answer)