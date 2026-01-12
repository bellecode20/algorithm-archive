#With GPT
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][d], d = 0: 가로, 1: 세로, 2: 대각선
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

# 시작 상태
dp[0][1][0] = 1

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            continue

        # 가로
        if dp[i][j][0]:
            if j+1 < n and data[i][j+1] == 0:
                dp[i][j+1][0] += dp[i][j][0]
            if i+1 < n and j+1 < n:
                if data[i][j+1] == 0 and data[i+1][j] == 0 and data[i+1][j+1] == 0:
                    dp[i+1][j+1][2] += dp[i][j][0]

        # 세로
        if dp[i][j][1]:
            if i+1 < n and data[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][1]
            if i+1 < n and j+1 < n:
                if data[i][j+1] == 0 and data[i+1][j] == 0 and data[i+1][j+1] == 0:
                    dp[i+1][j+1][2] += dp[i][j][1]

        # 대각선
        if dp[i][j][2]:
            if j+1 < n and data[i][j+1] == 0:
                dp[i][j+1][0] += dp[i][j][2]
            if i+1 < n and data[i+1][j] == 0:
                dp[i+1][j][1] += dp[i][j][2]
            if i+1 < n and j+1 < n:
                if data[i][j+1] == 0 and data[i+1][j] == 0 and data[i+1][j+1] == 0:
                    dp[i+1][j+1][2] += dp[i][j][2]

print(sum(dp[n-1][n-1]))