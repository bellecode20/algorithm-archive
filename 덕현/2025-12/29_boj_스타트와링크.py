'''
BOJ 14889 스타트와 링크

SWEA 햄버거 다이어트? 같은 문제

한 조합에 따른 다른 조합을 계속 추론

입력 :
N (짝수)
graph = list

구조 :
모든 경우의 수 비교 후 최솟값 출력 (절대값)

'''
def dfs(idx, cnt):
    global ans

    if cnt == N // 2:
        A = []
        B = []
        for i in range(N):
            if visit[i]:
                A.append(i)
            else:
                B.append(i)
        ij = 0
        ji = 0

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x, y = A[i], A[j]
                ij += graph[x][y] + graph[y][x]

        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                x, y = B[i], B[j]
                ji += graph[x][y] + graph[y][x]

        diff = ij - ji

        ans = min(ans, abs(diff))

        return

    for i in range(idx, N):
        if not visit[i]:
            visit[i] = 1
            dfs(i + 1, cnt + 1)
            visit[i] = 0



N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

ans = float('inf')
visit = [0] * N

dfs(0,0)
print(ans)