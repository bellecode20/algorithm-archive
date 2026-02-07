# https://www.acmicpc.net/problem/14719 (빗물)

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline


# left_max / right_max 배열 방식
def calc_rain_with_array(W, rain):
    left_max = [0] * W
    right_max = [0] * W

    left_max[0] = rain[0]
    right_max[W - 1] = rain[W - 1]

    # 왼쪽 최대
    for i in range(1, W):
        left_max[i] = max(rain[i], left_max[i - 1])

    # 오른쪽 최대
    for i in range(W - 2, -1, -1):
        right_max[i] = max(rain[i], right_max[i + 1])

    total = 0
    for i in range(W):
        total += min(left_max[i], right_max[i]) - rain[i]

    return total


# 투포인터 방식
def calc_rain_with_two_pointer(W, rain):
    l = 0
    r = W - 1

    left_max = rain[l]
    right_max = rain[r]

    total = 0

    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, rain[l])
            total += left_max - rain[l]
        else:
            r -= 1
            right_max = max(right_max, rain[r])
            total += right_max - rain[r]

    return total


# 입력
H, W = map(int, input().split())
rain = list(map(int, input().split()))

# 원하는 방식 선택해서 사용
print(calc_rain_with_array(W, rain))  # 배열 min, max O(n)
print(calc_rain_with_two_pointer(W, rain))  # 투포인터
