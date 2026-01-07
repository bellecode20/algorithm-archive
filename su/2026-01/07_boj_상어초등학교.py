# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

from collections import defaultdict

N = int(input())
info = defaultdict(list)
board = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0
scores = {
    0: 0,
    1: 1,
    2: 10,
    3: 100,
    4: 1000
}

for i in range(N**2):
    line = list(map(int, input().split()))
    a, b = line[0], line[1:]
    info[a] = b


for key, students in info.items():
    candidates = []  
    
    for r in range(N):
        for c in range(N):
            near_like = 0
            empty = 0
            if board[r][c] != 0:
                continue
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= N: 
                    continue
                if board[nr][nc] in students:
                    near_like += 1
                elif board[nr][nc] == 0:
                    empty += 1
            
            candidates.append((-near_like, -empty, r, c))
    
    candidates.sort()
    _, _, best_row, best_col = candidates[0]  # 정렬 후 첫번째 데이터 선택
    board[best_row][best_col] = key


# 만족도 조사
for r in range(N):
    for c in range(N):
            near_like = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= N: 
                    continue
                if board[nr][nc] in info[board[r][c]]:
                    near_like += 1
            
            answer += scores[near_like]

print(answer)