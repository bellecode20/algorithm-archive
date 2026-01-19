'''
BOJ 15685 드래곤 커브

입력:
N
x, y, d, g

구조:
- 드래곤 커브 방향 리스트만들기
- 0세대: [d]
- 다음 세대 만들기:
    기존 리스트를 뒤에서부터 보며 (dir + 1) % 4 를 append
- (x, y)에서 시작해 방향대로 한 칸씩 이동하야 점찍기
- 모든 커브를 그린 뒤, 네 점이 모두 찍힌 1*1 정사각형 개수 카운트


'''
# 우 상 좌 하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input().strip())
graph = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())

    dirs = [d]
    for _ in range(g):
        for k in range(len(dirs) - 1, -1, -1):
            dirs.append((dirs[k] + 1) % 4)

    graph[y][x] = 1
    cx, cy = x, y
    for nd in dirs:
        cx += dc[nd]
        cy += dr[nd]
        if 0 <= cx <= 100 and 0 <= cy <= 100:
            graph[cy][cx] = 1

ans = 0
for r in range(100):
    for c in range(100):
        if graph[r][c] and graph[r+1][c] and graph[r][c+1] and graph[r+1][c+1]:
            ans += 1

print(ans)
