from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
pos_r = pos_b = pos_g = (0, 0)

dr = [-1, 0, 1, 0]  # 위오아왼
dc = [0, 1, 0, -1]


for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            pos_r = r, c
            board[r][c] = "."
        elif board[r][c] == "B":
            pos_b = r, c
            board[r][c] = "."
        elif board[r][c] == "O":
            pos_g = r, c
            # board[r][c] = "."



def move_ball(row, col, dirc):
    turn = 0

    while True:
        nr, nc = row + dr[dirc], col + dc[dirc]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            break
        if board[nr][nc] == "#":
            break

        if (nr, nc) == pos_g:
            return (nr, nc), turn + 1
        
        row, col = nr, nc
        turn += 1

    return (row, col), turn



def tilt(red, blue, dirc):
    next_b, blue_cnt = move_ball(*blue, dirc)

    if next_b == pos_g:
        return None, None  # 빨간 공 움직일 필요도 없음
    

    next_red, red_cnt = move_ball(*red, dirc)

    # 위치 조정
    if next_red == pos_g:
        return next_red, next_b

    if next_b == next_red:
        if blue_cnt > red_cnt:  # blue가 더 뒤에 있었음
            next_b = (next_b[0] - dr[dirc], next_b[1] - dc[dirc])
        else:
            next_red = (next_red[0] - dr[dirc], next_red[1] - dc[dirc])

    return next_red, next_b



def solve():
    queue = deque([])
    queue.append((0, pos_r, pos_b))

    visited = set()
    visited.add((*pos_r, *pos_b))


    while queue:
        turn, r_pos, b_pos = queue.popleft()

        if turn >= 10:
            break
        
        for dirc in range(4):
            next_r, next_b = tilt(r_pos, b_pos, dirc)
            if next_b is None:
                continue
            
            if next_r == pos_g:
                return turn + 1

            if (*next_r, *next_b) not in visited:      
                queue.append((turn + 1, next_r, next_b))      
                visited.add((*next_r, *next_b))

    return -1


print(solve())
