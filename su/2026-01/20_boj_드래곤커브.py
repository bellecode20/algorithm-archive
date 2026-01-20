# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


N = int(input())
board = [[0] * 101 for _ in range(101)]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]  # 오 위 왼 아 방향 설정
answer = 0
gen = {}

gen[0] = [0]
gen[1] = [0, 1]

# 2세대부터는 [직전 세대] + [직전 세대 역순으로 돌면서 왼쪽으로 회전한 값]
for i in range(2, 11):
    temp = []
    for j in range(len(gen[i-1])-1, -1, -1):  # 역순으로
        temp.append((gen[i-1][j] + 1) % 4)  # 왼쪽으로 회전

    gen[i] = gen[i - 1] + temp


for _ in range(N):
    x, y, d, g =  map(int, input().split())  # x y시작점, d시작방향, g세대
    # x:col, y:row
    board[y][x] = 1

    for dirc in gen[g]:
        real_dir = (dirc + d) % 4  # 현재 입력값 방향대로 보정 필요
        nx = x + dc[real_dir]
        ny = y + dr[real_dir]
        board[ny][nx] = 1
        x, y = nx, ny


for i in range(100):  # 101까지 하면 +1 했을 때 보드판 인덱스 에러 -> 100까지만 탐색
    for j in range(100): 
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            answer += 1

print(answer)