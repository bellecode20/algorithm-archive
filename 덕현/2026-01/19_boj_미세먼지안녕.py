'''
BOJ 17144 미세먼지 안녕

입력:
R, C, T
graph (RxC)
-1 = 공기청정기

구조:
T번 반복
1) 확산:
   - 각 칸의 먼지 x는 인접 4방향(경계 안, 공기청정기 제외)으로 x//5 만큼 확산
   - 원래 칸은 (확산한 칸 수) * (x//5) 만큼 감소
   - 동시에 일어나므로 tmp에 누적

2) 공기청정기 작동:
   - 위쪽(반시계): 위로 -> 오른쪽 -> 아래로 -> 왼쪽 순환
   - 아래쪽(시계): 아래로 -> 오른쪽 -> 위로 -> 왼쪽 순환
   - 청정기 바로 오른쪽 칸은 0이 됨

'''

R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

purifier = []
for i in range(R):
    if graph[i][0] == -1:
        purifier.append(i)
up = purifier[0]
down = purifier[1]

def spread():
    tmp = [[0] * C for _ in range(R)]
    tmp[up][0] = -1
    tmp[down][0] = -1

    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                amt = graph[r][c] // 5
                if amt == 0:
                    tmp[r][c] += graph[r][c]
                    continue

                cnt = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != -1:
                        tmp[nr][nc] += amt
                        cnt += 1
                tmp[r][c] += graph[r][c] - amt * cnt
    return tmp

def run_purifier():
    # 위(반시계)
    for r in range(up - 1, 0, -1):
        graph[r][0] = graph[r - 1][0]
    for c in range(0, C - 1):
        graph[0][c] = graph[0][c + 1]
    for r in range(0, up):
        graph[r][C - 1] = graph[r + 1][C - 1]
    for c in range(C - 1, 1, -1):
        graph[up][c] = graph[up][c - 1]
    graph[up][1] = 0

    # 아래(시계)
    for r in range(down + 1, R - 1):
        graph[r][0] = graph[r + 1][0]
    for c in range(0, C - 1):
        graph[R - 1][c] = graph[R - 1][c + 1]
    for r in range(R - 1, down, -1):
        graph[r][C - 1] = graph[r - 1][C - 1]
    for c in range(C - 1, 1, -1):
        graph[down][c] = graph[down][c - 1]
    graph[down][1] = 0

    graph[up][0] = -1
    graph[down][0] = -1

for _ in range(T):
    graph = spread()
    run_purifier()

ans = 0
for r in range(R):
    for c in range(C):
        if graph[r][c] > 0:
            ans += graph[r][c]
print(ans)
