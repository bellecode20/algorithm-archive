dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
fireballs = []

for _ in range(m):
    r, c, mm, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, mm, s, d))

for _ in range(k):
    data = [[[] for _ in range(n)] for _ in range(n)]

    for r, c, mm, s, d in fireballs:
        nr = (r + dr[d] * (s % n)) % n
        nc = (c + dc[d] * (s % n)) % n
        data[nr][nc].append((mm, s, d))

    new_fireballs = []

    for r in range(n):
        for c in range(n):
            if not data[r][c]:
                continue

            if len(data[r][c]) == 1:
                mm, s, d = data[r][c][0]
                new_fireballs.append((r, c, mm, s, d))
            else:
                total_m = sum(f[0] for f in data[r][c])
                total_s = sum(f[1] for f in data[r][c])
                cnt = len(data[r][c])

                nm = total_m // 5
                if nm == 0:
                    continue

                ns = total_s // cnt

                even = all(f[2] % 2 == 0 for f in data[r][c])
                odd = all(f[2] % 2 == 1 for f in data[r][c])

                if even or odd:
                    dirs = [0, 2, 4, 6]
                else:
                    dirs = [1, 3, 5, 7]

                for d in dirs:
                    new_fireballs.append((r, c, nm, ns, d))

    fireballs = new_fireballs

print(sum(f[2] for f in fireballs))
