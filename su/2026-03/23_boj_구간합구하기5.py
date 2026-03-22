import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(n + 1)]  # N+1 크기

# 누적 합 계산
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 현재 칸 = 위쪽 + 왼쪽 - 대각선(중복) + 현재 그래프 값
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

# 구간 합 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 구간 합 공식: 전체 - 위쪽 - 왼쪽 + 대각선(중복 제거분 복구)
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)