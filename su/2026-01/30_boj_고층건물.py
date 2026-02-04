# 나무 재테크 https://www.acmicpc.net/problem/16235

# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


N = int(input())
buildings = list(map(int, input().split()))

answer = 0

for i in range(N):
    cnt = 0

    # 오른쪽
    max_slope = -float('inf')
    for j in range(i+1, N):
        slope = (buildings[j] - buildings[i]) / (j - i)
        if slope > max_slope:
            cnt += 1
            max_slope = slope
    
    min_slope = float('inf')
    for j in range(i - 1, -1, -1):
        slope = (buildings[j] - buildings[i]) / (j - i)
        if slope < min_slope:
            cnt += 1
            min_slope = slope
    
    answer = max(answer, cnt)

print(answer)
