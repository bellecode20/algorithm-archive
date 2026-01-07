n = int(input())
stu = []
like = dict()

for _ in range(n * n):
    data = list(map(int, input().split()))
    stu.append(data[0])
    like[data[0]] = set(data[1:])

board = [[0] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for s in stu:
    candidates = []

    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                continue

            like_cnt = 0
            empty_cnt = 0

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] in like[s]:
                        like_cnt += 1
                    elif board[nr][nc] == 0:
                        empty_cnt += 1

            candidates.append(( -like_cnt, -empty_cnt, r, c ))

    candidates.sort()
    r, c = candidates[0][2], candidates[0][3]
    board[r][c] = s

ans = 0
ans_lst = [0, 1, 10, 100, 1000]

for r in range(n):
    for c in range(n):
        s = board[r][c]
        cnt = 0

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] in like[s]:
                    cnt += 1

        ans += ans_lst[cnt]

print(ans)