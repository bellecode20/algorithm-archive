# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline
# from pprint import pprint

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def pprint(board):
    print('출력--------------------')
    for row in board:
        print(" ".join(map(str, row)))

answer = 0
visited = [[0] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, size, score):
    global answer
    if size == 4:
        answer = max(answer, score)
        return
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if visited[nr][nc]:
            continue

        if size == 2: 
            visited[nr][nc] = 1
            dfs(r, c, size + 1, score + graph[nr][nc])  # ㅗ 모양: 현재 좌표에서 분기점 추가
            visited[nr][nc] = 0

        visited[nr][nc] = 1
        dfs(nr, nc, size + 1, score + graph[nr][nc])
        visited[nr][nc] = 0


for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 1, graph[r][c])
        visited[r][c] = 0

print(answer)