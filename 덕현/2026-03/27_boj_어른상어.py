'''
BOJ 19237 어른 상어

입력:
N, M, K = map int input
grpah
dir
델타


구조:
냄새 배열 따로 관리
현재 냄새 기준으로 모든 상어 이동 방향 결정
이동 위치 모아서 작은 번호 상어만 남기기
냄새 1 감소
살아있는 상어 위치에 새 냄새 남기기
1번 상어만 남으면 시간 출력
1000초 넘으면 -1
'''
# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dirs = [0] + list(map(int, input().split()))

priority = [[[] for _ in range(5)] for _ in range(M + 1)]
for i in range(1, M + 1):
    for d in range(1, 5):
        priority[i][d] = list(map(int, input().split()))

shark = [[-1, -1, 0, 0] for _ in range(M + 1)]
alive = [False] * (M + 1)

for r in range(N):
    for c in range(N):
        if graph[r][c] != 0:
            num = graph[r][c]
            shark[num] = [r, c, dirs[num], 1]
            alive[num] = True

smell_num = []
smell_cnt = []
for _ in range(N):
    smell_num.append([0] * N)
    smell_cnt.append([0] * N)

for num in range(1, M + 1):
    if alive[num]:
        r, c, d, live = shark[num]
        smell_num[r][c] = num
        smell_cnt[r][c] = K

time = 0

while time <= 1000:

    cnt = 0
    for i in range(1, M + 1):
        if alive[i]:
            cnt += 1

    if cnt == 1 and alive[1]:
        print(time)
        break

    if time == 1000:
        print(-1)
        break

    nxt = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append([])
        nxt.append(row)

    for num in range(1, M + 1):
        if not alive[num]:
            continue

        r, c, d, live = shark[num]

        found = False
        nd = d
        nr = r
        nc = c

        for cur in priority[num][d]:
            tr = r + dr[cur - 1]
            tc = c + dc[cur - 1]

            if 0 <= tr < N and 0 <= tc < N:
                if smell_cnt[tr][tc] == 0:
                    nr = tr
                    nc = tc
                    nd = cur
                    found = True
                    break

        if not found:
            for cur in priority[num][d]:
                tr = r + dr[cur - 1]
                tc = c + dc[cur - 1]

                if 0 <= tr < N and 0 <= tc < N:
                    if smell_num[tr][tc] == num and smell_cnt[tr][tc] > 0:
                        nr = tr
                        nc = tc
                        nd = cur
                        break

        nxt[nr][nc].append((num, nd))

    for i in range(1, M + 1):
        if alive[i]:
            shark[i][3] = 0
            alive[i] = False

    for r in range(N):
        for c in range(N):
            if len(nxt[r][c]) == 0:
                continue

            nxt[r][c].sort()
            num, nd = nxt[r][c][0]
            shark[num] = [r, c, nd, 1]
            alive[num] = True

    for r in range(N):
        for c in range(N):
            if smell_cnt[r][c] > 0:
                smell_cnt[r][c] -= 1
                if smell_cnt[r][c] == 0:
                    smell_num[r][c] = 0

    for num in range(1, M + 1):
        if alive[num]:
            r, c, d, live = shark[num]
            smell_num[r][c] = num
            smell_cnt[r][c] = K

    time += 1