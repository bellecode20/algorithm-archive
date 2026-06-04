'''
프로그래머스 12913 땅따먹기

입력:
land

구조:
DP인듯 첫줄은 그대로 시작해도되고 두번째부터
이전 행 더하게하고 마지막에서 최대를 반환

'''


def solution(land):
    n = len(land)

    dp = []
    for i in range(n):
        dp.append([0] * 4)

    for c in range(4):
        dp[0][c] = land[0][c]

    for r in range(1, n):
        for c in range(4):
            num = 0

            for k in range(4):
                if c == k:
                    continue

                if dp[r - 1][k] > num:
                    num = dp[r - 1][k]

            dp[r][c] = num + land[r][c]

    ans = 0
    for c in range(4):
        if dp[n - 1][c] > ans:
            ans = dp[n - 1][c]

    return ans