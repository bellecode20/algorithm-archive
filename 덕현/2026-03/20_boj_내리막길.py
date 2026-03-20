'''
BOJ 1520 내리막 길

입력:
M
N
graph
dp
arr
구조:
dp?
시작점에서 각 칸까지 오는 경로 수 저장
높은 칸부터 정렬
현재 칸에서 더 낮은 칸으로 경로 수 넘기기
마지막 칸 출력
'''
# 하상우좌
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

M, N = map(int, input().split())
graph = []

for _ in range(M):
    graph.append(list(map(int, input().split())))
dp = []
for i in range(M):
    dp.append([0] * N)
arr = []
for r in range(M):
    for c in range(N):
        arr.append((graph[r][c], r, c))

arr.sort(reverse=True)

dp[0][0] = 1

for cur, r, c in arr:
    if dp[r][c] == 0:

        continue

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < M and 0 <= nc < N:
            if graph[nr][nc] < graph[r][c]:
                dp[nr][nc] += dp[r][c]

print(dp[M-1][N-1])