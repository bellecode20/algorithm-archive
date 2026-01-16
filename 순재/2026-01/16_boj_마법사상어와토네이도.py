#w. GPT
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

spread = {
    0: [(-1, 1, 1), (1, 1, 1), (-1, 0, 7), (1, 0, 7),
        (-2, 0, 2), (2, 0, 2), (-1, -1, 10), (1, -1, 10),
        (0, -2, 5)],
    1: [(-1, -1, 1), (-1, 1, 1), (0, -1, 7), (0, 1, 7),
        (0, -2, 2), (0, 2, 2), (1, -1, 10), (1, 1, 10),
        (2, 0, 5)],
    2: [(-1, -1, 1), (1, -1, 1), (-1, 0, 7), (1, 0, 7),
        (-2, 0, 2), (2, 0, 2), (-1, 1, 10), (1, 1, 10),
        (0, 2, 5)],
    3: [(1, -1, 1), (1, 1, 1), (0, -1, 7), (0, 1, 7),
        (0, -2, 2), (0, 2, 2), (-1, -1, 10), (-1, 1, 10),
        (-2, 0, 5)]
}

r = c = n // 2
d = 0
ans = 0
step = 1

while True:
    for _ in range(2):
        for _ in range(step):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0:
                print(ans)
                exit()

            sand = data[nr][nc]
            data[nr][nc] = 0
            used = 0

            for sr, sc, p in spread[d]:
                rr = nr + sr
                cc = nc + sc
                val = sand * p // 100
                used += val
                if 0 <= rr < n and 0 <= cc < n:
                    data[rr][cc] += val
                else:
                    ans += val

            ar = nr + dr[d]
            ac = nc + dc[d]
            alpha = sand - used
            if 0 <= ar < n and 0 <= ac < n:
                data[ar][ac] += alpha
            else:
                ans += alpha

            r, c = nr, nc
        d = (d + 1) % 4
    step += 1