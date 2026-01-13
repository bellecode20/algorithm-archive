# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


# 파이어볼개수: 2500
# 그래프: N*N = 250
# 연산 횟수 K: 1000
# 그래프에 직접 기록하면 매번 모든 칸 확인할 때 2500*250*1000 시간복잡도 높음
# -> 파어어볼 위치만 따로 딕셔너리로 저장하는 방식으로 하기

from collections import defaultdict

dirc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())
balls = defaultdict(list)

answer = 0

graph = [[[] * N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1  # 1부터 시작하므로 인덱스 조정
    c -= 1
    balls[(r, c)].append((m, s, d))


for k in range(K):

    new_balls = defaultdict(list)
    for key, item in balls.items():
        r, c = key
        for m, s, d in item:
            nr, nc = (r + dirc[d][0] * s) % N, (c + dirc[d][1] * s) % N
            new_balls[(nr, nc)].append((m, s, d))

    final_pos = defaultdict(list)
    for key, item in new_balls.items():
        cnt = len(item)
        if cnt < 2:
            final_pos[key].extend(item)
            continue

        sum_m, sum_s = 0, 0
        directions = set()  
        for m, s, d in item:
            sum_m += m
            sum_s += s
            directions.add(d % 2)

        nm, ns = sum_m // 5, sum_s // cnt
        
        if nm == 0:  # 질량이 0인 파이어볼
            continue

        if len(directions) == 1:  # 모두 홀수이거나 모두 짝수인경우
            for nd in range(0, 7, 2):
                final_pos[key].append((nm, ns, nd))
        else:
            for nd in range(1, 8, 2):  
                final_pos[key].append((nm, ns, nd))

    balls = final_pos  # 갱신

for key, item in final_pos.items():
    for m, _, _ in item:
        answer += m

print(answer)