'''
BOJ 2156 포도주 시식

입력:
n
graph

구조:
dp??
i번째 잔까지 봤을 때 최대값 저장
현재 잔을 안 마시는 경우 / 잔만 마시는 경우 / 현재 + 전 잔을 마시는 경우
셋 중 최대
'''
n = int(input())
graph = [0]

for _ in range(n):
    graph.append(int(input()))

if n == 1:
    print(graph[1])

elif n == 2:
    print(graph[1] + graph[2])

else:
    dp = [0] * (n + 1)

    dp[1] = graph[1]
    dp[2] = graph[1] + graph[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + graph[i], dp[i-3] + graph[i-1] + graph[i])

    print(dp[n])