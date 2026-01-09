# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline


from collections import defaultdict
from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(row, col):
    global visited, unions, index
    queue = deque([(row, col)])

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc] != 0:
                continue
            if (nr, nc) not in graph[(r, c)]:  # 국경이 안 열려있는 경우
                continue

            visited[nr][nc] = index
            unions[index].append((nr, nc))
            queue.append((nr, nc))


while True:
    graph = defaultdict(list)
    not_opened = True
    # 국경선 열기 (인접 리스트)
    for row in range(N):
        for col in range(N):
            for i in range(4):
                nr, nc = row + dr[i], col + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    continue
                if L <= abs(A[row][col] - A[nr][nc]) <= R:
                    graph[(row, col)].append((nr, nc))
                    graph[(nr, nc)].append((row, col))
                    not_opened = False

    if not_opened:
        break

    # 연합 찾기
    visited = [[0] * N for _ in range(N)]
    index = 1
    unions = defaultdict(list)

    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                visited[r][c] = index
                unions[index].append((r, c))
                bfs(r, c)
                index += 1
    
    # 인구 수 갱신
    for idx, pos in unions.items():
        population = 0
        cnt = len(pos)
        if len(pos) < 2:
            continue
        for r, c in pos:
            population += A[r][c]

        for r, c in pos:
            A[r][c] = population // cnt


    answer += 1

print(answer)