'''
BOJ 23290 마법사 상어와 복제

입력:
M, S
fish
smell


구조:
4x4
fish[r][c][d] = 그 칸에 d방향 물고기 수 (d:0~7)

'''

M, S = map(int, input().split())

fish = [[[0] * 8 for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(int, input().split())
    fish[r - 1][c - 1][d - 1] += 1

sr, sc = map(int, input().split())
sr -= 1
sc -= 1

smell = [[0] * 4 for _ in range(4)]

# 물고기 방향
fr = [0, -1, -1, -1, 0, 1, 1, 1]
fc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상,좌,하,우
sr4 = [-1, 0, 1, 0]
sc4 = [0, -1, 0, 1]

for _ in range(S):

    copy_fish = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in range(8):
                copy_fish[r][c][d] = fish[r][c][d]

    moved = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in range(8):
                cnt = fish[r][c][d]
                if cnt == 0:
                    continue

                nd = d
                ok = False
                for _rot in range(8):
                    nr = r + fr[nd]
                    nc = c + fc[nd]
                    if 0 <= nr < 4 and 0 <= nc < 4:
                        if not (nr == sr and nc == sc) and smell[nr][nc] == 0:
                            moved[nr][nc][nd] += cnt
                            ok = True
                            break
                    nd = (nd - 1) % 8

                if not ok:
                    moved[r][c][d] += cnt

    fish = moved

    best_eat = -1
    best_path = None

    for a in range(4):
        r1 = sr + sr4[a]
        c1 = sc + sc4[a]
        if not (0 <= r1 < 4 and 0 <= c1 < 4):
            continue

        for b in range(4):
            r2 = r1 + sr4[b]
            c2 = c1 + sc4[b]
            if not (0 <= r2 < 4 and 0 <= c2 < 4):
                continue

            for cdir in range(4):
                r3 = r2 + sr4[cdir]
                c3 = c2 + sc4[cdir]
                if not (0 <= r3 < 4 and 0 <= c3 < 4):
                    continue

                seen = set()
                eat = 0

                if (r1, c1) not in seen:
                    seen.add((r1, c1))
                    eat += sum(fish[r1][c1])
                if (r2, c2) not in seen:
                    seen.add((r2, c2))
                    eat += sum(fish[r2][c2])
                if (r3, c3) not in seen:
                    seen.add((r3, c3))
                    eat += sum(fish[r3][c3])

                if eat > best_eat:
                    best_eat = eat
                    best_path = (a, b, cdir)

    a, b, cdir = best_path
    for d in (a, b, cdir):
        sr += sr4[d]
        sc += sc4[d]
        if sum(fish[sr][sc]) > 0:
            fish[sr][sc] = [0] * 8
            smell[sr][sc] = 3
    for r in range(4):
        for c in range(4):
            if smell[r][c] > 0:
                smell[r][c] -= 1

    for r in range(4):
        for c in range(4):
            for d in range(8):
                fish[r][c][d] += copy_fish[r][c][d]

ans = 0
for r in range(4):
    for c in range(4):
        ans += sum(fish[r][c])

print(ans)