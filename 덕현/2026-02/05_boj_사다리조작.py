'''
BOJ 15684 사다리 조작

입력:
N, M, H

구조:
- graph[r][c] = 1 이면 r번째 줄에서 c -> c+1
- 위에서 아래로 내려가면서 좌우 이동
- 최대 3개까지 가로선 추가
'''



def check():
    for s in range(1, N + 1):
        cur = s
        for r in range(1, H + 1):
            if graph[r][cur]:
                cur += 1
            elif cur > 1 and graph[r][cur - 1]:
                cur -= 1
        if cur != s:
            return 0
    return 1


def dfs(pos, cnt, limit):
    global ans

    if cnt == limit:
        if check():
            ans = limit
        return

    for k in range(pos, H * (N - 1)):
        r = k // (N - 1) + 1
        c = k % (N - 1) + 1

        if graph[r][c]:
            continue
        if c > 1 and graph[r][c - 1]:
            continue
        if c < N - 1 and graph[r][c + 1]:
            continue

        graph[r][c] = 1
        dfs(k + 1, cnt + 1, limit)
        graph[r][c] = 0

        if ans != 4:
            return


N, M, H = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1


ans = 4

for limit in range(4):
    dfs(0, 0, limit)
    if ans != 4:
        break

if ans != 4:
    print(ans)
else:
    print(-1)
