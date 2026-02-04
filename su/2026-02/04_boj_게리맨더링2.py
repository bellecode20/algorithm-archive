# https://www.acmicpc.net/problem/17779
# 입력 텍스트 파일 실행 코드

'''
히든 테케
9
100 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 100

-> 77 출력해야 함
'''

import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "../input.txt", "r")
input = sys.stdin.readline


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
answer = INF


def calculate(x, y, d1, d2):
    """
    (x, y, d1, d2)가 주어졌을 때
    5개 구역으로 나누고 인구 차이를 반환
    """
    # 구역 번호 저장 (0: 미정, 1~5: 선거구)
    district = [[0] * N for _ in range(N)]

    # 경계선(5번 선거구) 표시
    for i in range(d1 + 1):
        district[x + i][y - i] = 5
        district[x + d2 + i][y + d2 - i] = 5

    for i in range(d2 + 1):
        district[x + i][y + i] = 5
        district[x + d1 + i][y - d1 + i] = 5

    # 경계 내부 채우기 (5번 선거구)
    for r in range(x + 1, x + d1 + d2):
        fill = False
        for c in range(N):
            if district[r][c] == 5:
                fill = not fill
            elif fill:
                district[r][c] = 5

    # 나머지 선거구 채우기.
    for r in range(x + d1):
        for c in range(y + 1):
            if district[r][c] == 5: break
            district[r][c] = 1

    for r in range(x + d2 + 1):
        for c in range(N - 1, y, -1):
            if district[r][c] == 5: break
            district[r][c] = 2

    for r in range(x + d1, N):
        for c in range(y - d1 + d2):
            if district[r][c] == 5: break
            district[r][c] = 3

    for r in range(x + d2 + 1, N):
        for c in range(N - 1, y - d1 + d2 - 1, -1):
            if district[r][c] == 5: break
            district[r][c] = 4


    # 인구 계산
    population = [0] * 5
    for r in range(N):
        for c in range(N):
            population[district[r][c] - 1] += A[r][c]

    return max(population) - min(population)


# 모든 경우 탐색
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                # 범위 체크
                if x + d1 + d2 >= N:
                    continue
                if y - d1 < 0 or y + d2 >= N:
                    continue

                answer = min(answer, calculate(x, y, d1, d2))

print(answer)