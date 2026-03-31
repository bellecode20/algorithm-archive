'''
BOJ 12865 평범한 배낭

입력:
N, K = map(int, input().split)
item

구조:
dp?
i번째 물건까지 봤을 때
무게 j에서 최대 가치 저장
현재 물건을 안 넣는 경우
현재 물건을 넣는 경우
둘 중 최대값 저장
'''
N, K = map(int, input().split())

item = []
for _ in range(N):
    w, v = map(int, input().split())
    item.append((w, v))

dp = []
for _ in range(N + 1):
    dp.append([0] * (K + 1))

for i in range(1, N + 1):
    w = item[i - 1][0]
    v = item[i - 1][1]

    for j in range(K + 1):
        dp[i][j] = dp[i - 1][j]

        if j >= w:
            if dp[i][j] < dp[i - 1][j - w] + v:
                dp[i][j] = dp[i - 1][j - w] + v

print(dp[N][K])