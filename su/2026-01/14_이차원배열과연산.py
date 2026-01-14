# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

# 
# 일부 테케 실패 수정 필요한 코드 입니다.
#

from copy import deepcopy
from collections import Counter

r, c, k = map(int, input().split())
graph = [[0] * 100 for _ in range(100)]
for i in range(3):
    graph[i][0], graph[i][1], graph[i][2] = map(int, input().split())

answer = -1

t = 0
def pprint(grp):
    for rr in range(len(grp)):
        print(grp[rr])
    
r -= 1
c -= 1

while t <= 100:
    if graph[r][c] == k:
        answer = t
        break

    lr = lc = 0
    for row_i in range(100):
        for col_i in range(100):
            if graph[row_i][col_i] != 0:
                lr = max(lr, row_i)
                lc = max(lc, col_i)

    print(f"lr: {lr}, lc: {lc}")
    new_graph = [[0] * 100 for _ in range(100)]

    if lr >= lc:

        for row in range(lr):
            print(f"row: {row}")
            rows = []
            
            for col in range(lc):
                if graph[row][col] == 0:
                    continue
                rows.append(graph[row][col])
            
            rows_counter = Counter(rows)
            candidates = []
            for key, item in rows_counter.items():
                candidates.append((key, item))
            candidates.sort(key=lambda x: (x[1], x[0]))  # 등장 횟수, 수

            gap = 0
            for i in range(len(candidates)):
                new_graph[row][gap] = candidates[i][0]
                new_graph[row][gap+1] = candidates[i][1]
                gap += 2
        
        print()
    else:
        for col in range(lc):
            cols = []
            print(f"col: {col}")
            for row in range(lr):
                if graph[row][col] == 0:
                    continue
                cols.append(graph[row][col])
            
            cols_counter = Counter(rows)
            candidates = []
            for key, item in cols_counter.items():
                candidates.append((key, item))
            candidates.sort(key=lambda x: (x[1], x[0]))  # 등장 횟수, 수

            gap = 0
            for i in range(len(candidates)):
                new_graph[gap][col] = candidates[i][0]
                new_graph[gap+1][col] = candidates[i][1]
                gap += 2

    graph = deepcopy(new_graph)
    pprint(graph)
    t += 1

print(answer)