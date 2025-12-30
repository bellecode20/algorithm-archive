#With GPT
import copy 

def move_fish(board, fishes, sr, sc):
    for fnum in range(1, 17):
        if fishes[fnum][2] == -1:
            continue
        r, c, d = fishes[fnum]
        for _ in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4 and not (nr == sr and nc == sc):
                target = board[nr][nc]
                if target != 0:
                    fishes[target][0], fishes[target][1] = r, c
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                fishes[fnum] = [nr, nc, d]
                break
            d = (d + 1) % 8
        else:
            fishes[fnum][2] = d

def dfs(board, fishes, sr, sc, score):
    global ans
    board = copy.deepcopy(board)
    fishes = copy.deepcopy(fishes)

    fnum = board[sr][sc]
    score += fnum

    shark_dir = fishes[fnum][2]
    fishes[fnum][2] = -1
    board[sr][sc] = 0

    move_fish(board, fishes, sr, sc)

    ans = max(ans, score)
    for step in range(1, 4):
        nr = sr + dr[shark_dir] * step
        nc = sc + dc[shark_dir] * step

        if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc] != 0:
            dfs(board, fishes, nr, nc, score)


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

board = [[0]*4 for _ in range(4)]
fishes = [[0,0,0] for _ in range(17)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        num, di = data[2*j], data[2*j+1]-1
        board[i][j] = num
        fishes[num] = [i, j, di]

ans = 0
dfs(board, fishes, 0, 0, 0)
print(ans)
