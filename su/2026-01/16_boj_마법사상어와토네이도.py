import sys
input = sys.stdin.readline

# with GPT

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 토네이도 방향: 왼0, 아래1, 오른2, 위3
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

# 흩뿌리기 비율과 상대 좌표 (왼쪽 방향 패턴 기준, 나머지 방향은 변환)
sand_ratio = [
    (-1, 1, 0.01), (1, 1, 0.01),
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, -1, 0.1), (1, -1, 0.1),
    (0, -2, 0.05),
]

def rotate(r, c, d):
    # 방향에 맞게 상대 좌표 회전
    for _ in range(d):
        r, c = c, -r
    return r, c

def spread_sand(r, c, d):
    global ans
    sand = board[r][c]
    board[r][c] = 0
    ssum = 0

    for rr, cc, ratio in sand_ratio:
        nr, nc = r + rotate(rr, cc, d)[0], c + rotate(rr, cc, d)[1]
        amount = int(sand * ratio)
        ssum += amount
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] += amount
        else:
            ans += amount

    # α 모래
    ar, ac = r + dr[d], c + dc[d]
    alpha = sand - ssum
    if 0 <= ar < N and 0 <= ac < N:
        board[ar][ac] += alpha
    else:
        ans += alpha

# 시작점
r = c = N // 2
ans = 0

step = 1
direction = 0
while True:
    for _ in range(2):
        for _ in range(step):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if nr < 0 or nc < 0:
                print(ans)
                sys.exit(0)

            spread_sand(nr, nc, direction)
            r, c = nr, nc

        direction = (direction + 1) % 4
    step += 1
