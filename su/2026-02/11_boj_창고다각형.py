# 창고 다각형 https://www.acmicpc.net/problem/2304

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

'''
빗물 문제와 유사하게 풀이한다.
현재 인덱스를 기준으로 했을 때 
왼쪽 영역 중 제일 최댓값, 오른쪽 영역 중 제일 최댓값을 찾아낸 후
둘 중 더 작은 값을 지붕으로 선택한다.
'''

N = int(input())
H = [0] * 1001

minX = 1000
maxX = 0

for _ in range(N):
    x, h = map(int, input().split())
    H[x] = h
    
    if x < minX:
        minX = x
    if x > maxX:
        maxX = x

left_max = [0] * 1001
right_max = [0] * 1001

left_max[minX] = H[minX]
right_max[maxX] = H[maxX]

cur = 0
for x in range(minX + 1, maxX + 1):
    left_max[x] = max(left_max[x-1], H[x])  # 이전까지의 최대 높이와 현재 높이를 비교하면서 최대높이 갱신  

cur = 0
for x in range(maxX - 1, minX - 1, -1):
    right_max[x] = max(right_max[x+1], H[x])

area = 0
for x in range(minX, maxX + 1):
    area += min(left_max[x], right_max[x])  # 가장 작은 창고 다각형을 구해야 하므로 낮은 높이를 선택함


print(area)