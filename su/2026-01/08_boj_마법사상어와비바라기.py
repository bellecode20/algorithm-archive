# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


from copy import deepcopy
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]  # 물의 양
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diamonds = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
# 비구름 위치
cloud =  {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}  # 0 ~ N-1 범위로 인덱스 조정
answer = 0

for m in range(M):
    d, s = map(int, input().split())
    d -= 1
    moved_cloud = set()
    new_board = [[0] * N for _ in range(N)]

    for r, c in cloud:
        nr, nc = r + directions[d][0] * s, c + directions[d][1] * s
        nr = (nr + (s * N)) % N  # 격자 밖인 케이스 고려해서 보정
        nc = (nc + (s * N)) % N
        moved_cloud.add((nr, nc))
        A[nr][nc] += 1  # 물의 양 1 증가
    
    watered_A = deepcopy(A)  
    for r, c, in moved_cloud:
        water = 0
        for i in range(4):
            nr, nc = r + diamonds[i][0], c + diamonds[i][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if A[nr][nc] == 0:  # 물이 없는 경우
                continue
            water += 1
        watered_A[r][c] += water # A를 참조하면서 A를 수정하면 오류 생기므로 복사해놓은 A를 수정함
    
    # 새로 생길 구름들
    new_cloud = set()
    final_A = deepcopy(watered_A)
    for row in range(N):
        for col in range(N):
            if watered_A[row][col] >= 2 and (row, col) not in moved_cloud:
                new_cloud.add((row, col))
                final_A[row][col] -= 2

    cloud = new_cloud
    A = final_A

for r in range(N):
    for c in range(N):
        answer += A[r][c]

print(answer)