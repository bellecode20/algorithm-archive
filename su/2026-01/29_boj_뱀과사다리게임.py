
# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

'''

'''

from collections import deque

def solve():
    N, M = map(int, input().split())

    # 사다리 / 뱀 정보
    warp = [0] * 101
    for _ in range(N + M):
        a, b = map(int, input().split())
        warp[a] = b

    # dist[i] = i번 칸까지 도달하는 최소 주사위 횟수
    dist = [-1] * 101
    q = deque()

    dist[1] = 0
    q.append(1)

    while q:
        cur = q.popleft()

        if cur == 100:
            print(dist[cur])
            return

        for dice in range(1, 7):
            nxt = cur + dice
            if nxt > 100:
                continue

            # 사다리 or 뱀 있으면 즉시 이동
            if warp[nxt] != 0:
                nxt = warp[nxt]

            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

solve()
