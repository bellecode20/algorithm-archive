# 창고 다각형 https://www.acmicpc.net/problem/2304

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline

'''
N개의 막대 기둥이 일렬로 세워져 있다.
지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
지붕의 가장자리는 땅에 닿아야 한다.
비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.


'''

N = int(input())
H = [0] * 1001

minX = 1000
maxX = 0

for _ in range(N):
    x, h = map(int, input().split())
    if h > H[x]:
        H[x] = h
    if x < minX:
        minX = x
    if x > maxX:
        maxX = x

left_max = [0] * 1001
right_max = [0] * 1001

cur = 0
for x in range(minX, maxX + 1):
    if H[x] > cur:
        cur = H[x]
    left_max[x] = cur

cur = 0
for x in range(maxX, minX - 1, -1):
    if H[x] > cur:
        cur = H[x]
    right_max[x] = cur

area = 0
for x in range(minX, maxX + 1):
    area += min(left_max[x], right_max[x])

print(area)
