# 트럭 https://www.acmicpc.net/problem/13335

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline


from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * w)
time = 0
load = 0

while bridge:
    cur_w = bridge.popleft()
    load -= cur_w

    if trucks:
        if load + trucks[0] <= L:
            next_w = trucks.popleft()
            bridge.append(next_w)
            load += next_w
        else:
            bridge.append(0)
            
    time += 1
            
print(time)