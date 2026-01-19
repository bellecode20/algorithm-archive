'''
BOJ 20057 마법사 상어와 토네이도

입력:
N
graph (NxN)

구조:
- 토네이도는 (N//2, N//2)에서 시작
- 이동 방향: 왼쪽 -> 아래 -> 오른쪽 -> 위 (달팽이)
- 각 칸으로 이동할 때, 그 칸의 모래를 맞춰서 뿌리기
- 격자 밖 == 나간 모래의 총합 출력
- 달팽이 이동 경로 생성: step = 1,1,2,2,3,3...
- 매 이동마다:
   - nx, ny로 이동
   - spread(nx, ny, dir)

'''
dr = [0, 1, 0, -1]   # 좌하우상
dc = [-1, 0, 1, 0]
base = [
    (-1, 1, 1), (1, 1, 1),
    (-1, 0, 7), (1, 0, 7),
    (-2, 0, 2), (2, 0, 2),
    (-1, -1, 10), (1, -1, 10),
    (0, -2, 5),
]


def rotate(y, x, d):
    if d == 0:
        return y, x
    if d == 1:
        return -x, y
    if d == 2:
        return -y, -x
    return x, -y


def spread(r, c, d):
    global out_sand
    sand = graph[r][c]
    if sand == 0:
        return
    graph[r][c] = 0

    moved = 0
    for y, x, p in base:
        ry, rx = rotate(y, x, d)
        nr = r + ry
        nc = c + rx
        amount = (sand * p) // 100
        moved += amount

        if 0 <= nr < N and 0 <= nc < N:
            graph[nr][nc] += amount
        else:
            out_sand += amount

    ar = r + dr[d]
    ac = c + dc[d]
    alpha = sand - moved
    if 0 <= ar < N and 0 <= ac < N:
        graph[ar][ac] += alpha
    else:
        out_sand += alpha

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

out_sand = 0
r = c = N // 2

step = 1
d = 0
while True:
    for _ in range(2):
        for _ in range(step):
            nr = r + dr[d]
            nc = c + dc[d]
            r, c = nr, nc
            spread(r, c, d)

            if r == 0 and c == 0:
                print(out_sand)
                raise SystemExit
        d = (d + 1) % 4
    step += 1
