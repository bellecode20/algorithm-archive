import sys

# python3로 제출해야 메모리 초과 오류 발생하지 않음
# 재귀 깊이 제한을 늘려주어야 RecursionError를 방지할 수 있습니다.
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve():
    # M: 세로 크기, N: 가로 크기
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    
    # dp[y][x]는 (y, x)에서 목적지까지 갈 수 있는 경로의 수
    # -1은 아직 방문하지 않았음을 의미합니다.
    dp = [[-1] * N for _ in range(M)]

    # 이동 방향 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def dfs(y, x):
        # 1. 목적지에 도달하면 경로 1개를 찾은 것이므로 1을 반환
        if y == M - 1 and x == N - 1:
            return 1

        # 2. 이미 계산된 적이 있다면(수첩에 적혀 있다면) 그 값을 즉시 반환
        if dp[y][x] != -1:
            return dp[y][x]

        # 3. 처음 방문하는 곳이라면 일단 0으로 초기화하고 탐색 시작
        dp[y][x] = 0

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 격자 내부에 있고, 내리막길인 경우에만 이동
            if 0 <= ny < M and 0 <= nx < N:
                if grid[ny][nx] < grid[y][x]:
                    # 하위 경로에서 반환된 값(성공 횟수)을 현재 칸에 누적
                    dp[y][x] += dfs(ny, nx)

        # 4. 주변 탐색을 모두 마친 후, 수집된 경로의 총합을 위로 전달
        return dp[y][x]

    # (0, 0)에서 시작하는 경로의 총 개수 출력
    print(dfs(0, 0))

solve()