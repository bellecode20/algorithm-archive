# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


from copy import deepcopy
R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
answer = 0
machine = []
for r in range(R):
    for c in range(C):
        if A[r][c] == -1:
            machine.append((r, c))

def spread_dust(sr, sc, A, spread_a):
    dr = [0, -1, 0, 1]  # 오 위 왼 아
    dc = [1, 0, -1, 0]
    cnt = 0
    cells = []
    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            continue
        if A[nr][nc] == -1:  # 공청기
            continue
        cnt += 1
        cells.append((nr, nc))
    
    for row, col in cells:
        spread_a[row][col] += A[sr][sc] // 5

    spread_a[sr][sc] += A[sr][sc] - ((A[sr][sc] // 5) * cnt)


def run_machine(di, A, new_A):  # di: 0윗부분, 1아랫부분
    if di == 0:
        br = [0, -1, 0, 1]  # 오 위 왼 아
        bc = [1, 0, -1, 0]  
    elif di == 1:
        br = [0, 1, 0, -1]  # 오 아 왼 위
        bc = [1, 0, -1, 0]  
    
    turn = 0
    m_row, m_col = machine[di][0], machine[di][1]
    sr, sc = m_row, m_col + 1
    new_A[sr][sc] = 0
    while True:
        nr, nc = sr + br[turn], sc + bc[turn]
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            turn += 1
            nr, nc = sr + br[turn], sc + bc[turn]
        if new_A[nr][nc] == -1:
            break
        
        new_A[nr][nc] = A[sr][sc]
        sr, sc = nr, nc    

for _ in range(T):
    spread_a = [[0] * C for _ in range(R)]
    for mr, mc in machine:
        spread_a[mr][mc] = -1

    # 1단계: 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if A[r][c] > 0:
                spread_dust(r, c, A, spread_a)

    A = spread_a  # 확산된 그래프로 변경

    new_A = deepcopy(A)  # 순환 영역 제외한 다른 미세먼지는 그대로 있어야 함으로 0으로 초기화하지 않고 기존 그래프 복사

    # 2단계: 공청기 순환
    run_machine(0, A, new_A)  # 윗부분
    run_machine(1, A, new_A)  # 아랫부분
    

    A = new_A

for r in range(R):
    for c in range(C):
        if A[r][c] > 0:
            answer += A[r][c]
print(answer)