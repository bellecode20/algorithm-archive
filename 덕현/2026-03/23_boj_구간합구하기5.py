'''
BOJ 11660 구간 합 구하기 5

입력:
N, M
graph
dp

구조:
누적합 구해보기
dp r c 에 1 1 부터 (r,c)까지 합 저장
결과?

'''
N, M = map(int, input().split())

graph = [[0] * (N + 1)]
for _ in range(N):
    graph.append([0] + list(map(int, input().split())))

dp = []
for _ in range(N+1):
    dp.append([0]*(N + 1))

for r in range(1, N + 1):
    for c in range(1, N + 1):
        dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + graph[r][c]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)