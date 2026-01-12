'''
BOJ 17070 파이프 옮기기 1

입력 :
N
graph

구조 :
dp[r][c][dir] = (r,c)를 파이프 "끝점"으로 두고 dir 방향일 때 경우의 수
dir = 0(가로), 1(세로), 2(대각)

- 가로: (r, c+1) 가능
- 세로: (r+1, c) 가능
- 대각: (r, c+1), (r+1, c), (r+1, c+1) 모두 0일 때 가능
'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            continue

        if c + 1 < N and graph[r][c+1] == 0:
            dp[r][c+1][0] += dp[r][c][0] + dp[r][c][2]

        if r + 1 < N and graph[r+1][c] == 0:
            dp[r+1][c][1] += dp[r][c][1] + dp[r][c][2]

        if r + 1 < N and c + 1 < N:
            if graph[r][c+1] == 0 and graph[r+1][c] == 0 and graph[r+1][c+1] == 0:
                dp[r+1][c+1][2] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]

print(sum(dp[N-1][N-1]))
