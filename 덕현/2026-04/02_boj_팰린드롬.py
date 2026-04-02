'''
BOJ 10942 팰린드롬?

입력:
N
arr
M
s,e = map(int,input().split())

구조:
앞이랑 뒤에서 비교해서 맞으면 맞고 아니면 아니게 - 시간초과

dp로 해야됨
기존에 검사했던곳 맞는지 확인하고 맞으면 나머지만 비교하면됨. 그걸 기어갷두면될듯

길이까지저정하고
질문은 정답 배열에 담았다가 한 번에 출력하면 타임아웃 안난다해서 됨
'''
N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())

dp = []
for _ in range(N + 1):
    dp.append([0] * (N + 1))

for i in range(1, N + 1):
    dp[i][i] = 1

for i in range(1, N):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1

for gap in range(2, N):
    for s in range(1, N - gap + 1):
        e = s + gap

        if arr[s] == arr[e] and dp[s + 1][e - 1] == 1:
            dp[s][e] = 1

ans = []

for _ in range(M):
    s, e = map(int, input().split())
    ans.append(str(dp[s][e]))

print('\n'.join(ans))