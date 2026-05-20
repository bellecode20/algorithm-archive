'''
프로그래머스 154538 숫자 변환하기

입력:
x y n

구조:
dp x부터 y까지 돌기
가능하면 3개 되면 dp[y]
안되면 answer -1
'''
def solution(x, y, n):
    dp = []
    for i in range(y + 1):
        dp.append(float('inf'))

    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue
        num = i + n
        if num <= y:
            if dp[num] > dp[i] + 1:
                dp[num] = dp[i] + 1
        num = i * 2
        if num <= y:
            if dp[num] > dp[i] + 1:
                dp[num] = dp[i] + 1
        num = i * 3
        if num <= y:
            if dp[num] > dp[i] + 1:
                dp[num] = dp[i] + 1

    if dp[y] == float('inf'):
        return -1

    return dp[y]