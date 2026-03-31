N, K = map(int, input().split())  # 4, 7
items = [list(map(int, input().split())) for _ in range(N)]

def dp_1():  # 역순
    dp = [0] * (K + 1)

    for item in items:
        weight, value = item
        for i in range(K, weight - 1, -1):  # 현재 무게까지
            dp[i] = max(dp[i], dp[i - weight] + value)

    print(dp[-1])


def dp_2():  # 정방향
    dp = [[0] * (K + 1) for _ in range(N + 1)]  # dp[물건개수+1][최대무게+1]

    for i in range(1, N + 1):
        weight, value = items[i-1]

        for j in range(1, K + 1):  # 배낭의 무게
            if weight <= j:
                # i번째 물건을 넣는 경우 vs 안 넣는 경우
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            else:
                # 무게가 넘쳐서 못 넣는 경우
                dp[i][j] = dp[i-1][j]

    print(dp[-1][-1])

dp_1()
dp_2()
