'''
boj 19236 청소년 상어

상어 이동 후 물고기 이동을 전체적으로 하는 것
그리고 그 물고기들의 번호의 합 적기

델타 8방향 1부터 입력이 주어지므로 0번에는 (0,0)


입력 :
num_fish, dir_fish 홀짝으로 받기

'''
from copy import deepcopy

dr = [0,-1,-1,0,1,1,1,0,-1]
dc = [0,0,-1,-1,-1,0,1,1,1]

def move_fish(nf, df, sx, sy):
    for fish in range(1, 17):
        found = False

        for i in range(4):
            for j in range(4):
                if nf[i][j] == fish:
                    x, y = i, j
                    d = df[i][j]
                    found = True
                    break
            if found:
                break

        if not found:
            continue

        for _ in range(8):
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == sx and ny == sy):
                nf[x][y], nf[nx][ny] = nf[nx][ny], nf[x][y]
                df[x][y], df[nx][ny] = df[nx][ny], d
                break

            d = d % 8 + 1

def dfs(nf, df, sx, sy, sd, total):
    global ans
    ans = max(ans, total)

    move_fish(nf, df, sx, sy)

    for step in range(1, 4):
        nx = sx + dr[sd] * step
        ny = sy + dc[sd] * step

        if not (0 <= nx < 4 and 0 <= ny < 4):
            break

        if nf[nx][ny] == 0:
            continue

        nf2 = deepcopy(nf)
        df2 = deepcopy(df)

        fish_num = nf2[nx][ny]
        nd = df2[nx][ny]

        nf2[nx][ny] = 0
        df2[nx][ny] = 0

        dfs(nf2, df2, nx, ny, nd, total + fish_num)

graph = [list(map(int,input().split())) for _ in range(4)]

num_fish = [[] for _ in range(4)]
dir_fish = [[] for _ in range(4)]
ans = 0

for i in range(4):
    for j in range(8):
        if (j % 2) == 0:
            num_fish[i].append(graph[i][j])
        else:
            dir_fish[i].append(graph[i][j])

start_sum = num_fish[0][0]
start_dir = dir_fish[0][0]

num_fish[0][0] = 0
dir_fish[0][0] = 0

dfs(num_fish, dir_fish, 0, 0, start_dir, start_sum)

print(ans)