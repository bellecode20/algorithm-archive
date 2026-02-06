# https://www.acmicpc.net/problem/13458
# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

# 수정 중인 코드입니다.

H, W = map(int, input().split())
rain = list(map(int, input().split()))
result = [0] * W
start_i = 0

while start_i < W - 1:
    end_i = start_i + 1
    max_h = rain[end_i]

    while end_i < W:
        max_h = max(max_h, rain[end_i])
        
        if rain[end_i] >= rain[start_i]:  
            break
        
        end_i += 1
    
    line = min(max_h, rain[start_i])
    for i in range(start_i + 1, end_i):
        result[i] += line - rain[i]
    start_i = end_i


print(sum(result))
