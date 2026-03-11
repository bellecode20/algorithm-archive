'''
프로그래머스 389480 완전범죄

입력:
info
A
B

구조:
dp[j] = B 흔적이 j일 때 A 흔적 최소
물건마다 A가 훔치는 경우, B가 훔치는 경우 생각
마지막 가능한 dp 중 최소 찾기
'''
def solution(info, n, m):
    INF = float('inf')

    dp = [INF] * m
    dp[0] = 0

    for i in range(len(info)):
        a = info[i][0]
        b = info[i][1]

        nxt = [INF] * m

        for j in range(m):
            if dp[j] == INF:
                continue
            # A훔
            if dp[j] + a < n:
                if nxt[j] > dp[j] + a:
                    nxt[j] = dp[j] + a
            # B훔
            if j + b < m:
                if nxt[j + b] > dp[j]:
                    nxt[j + b] = dp[j]

        dp = nxt

    ans = float('inf')
    for j in range(m):
        if ans > dp[j]:
            ans = dp[j]

    if ans == INF:
        return -1

    return ans