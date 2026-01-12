# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 해설 참고하여 풀이하였음

from collections import defaultdict, deque
from copy import deepcopy

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0


dp = [[[0] * 3 for _ in range(N)] for _ in range(N) ]
dp[0][1][0] = 1

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            continue

        # 0: 가로
        if c - 1 >= 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]

        # 1: 세로
        if r - 1 >= 0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]

        # 2: 대각
        if r - 1 >= 0 and c - 1 >= 0:
            if graph[r-1][c] == 0 and graph[r][c-1] == 0:
                dp[r][c][2] += (
                    dp[r-1][c-1][0] +
                    dp[r-1][c-1][1] +
                    dp[r-1][c-1][2]
                )

print(sum(dp[N-1][N-1]))
