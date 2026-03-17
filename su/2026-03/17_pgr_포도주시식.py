N = int(input())
wine = [int(input()) for _ in range(N)]

answer = 0
dp = [[0] * 3 for _ in range(N)]
dp[0][1] = wine[0]

for i in range(1, N):
    for j in range(3):
        if j == 0:  # 이번 거 안 마심
            dp[i][j] = max(dp[i-1])
        elif j == 1:  # 이번 거 마심. 연속 1잔일 때(이전에 연속된거 없음)
            dp[i][j] = dp[i-1][0] + wine[i]
        elif j == 2:  # 이번 거 마심. 연속 2잔일 때
            dp[i][j] = dp[i-1][1] + wine[i]

answer = max(dp[N-1])
print(answer)