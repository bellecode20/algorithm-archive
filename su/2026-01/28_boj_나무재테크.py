# 나무 재테크 https://www.acmicpc.net/problem/16235

# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

'''
나무를 나이순으로 정렬하는 대신(리스트)
deque를 사용, popleft()와 appendleft()를 사용해 시간 복잡도 줄이기

N * N 크기의 땅
땅을 1*1 크기 칸으로 나누었다. (r, c는 1부터 시작) [warn]
양분 조사 -> 조사
처음에 양분은 모든 칸에 5만큼 들어있음

M개의 나무를 구매해 땅에 심었다.
같은 칸에 나무 여러개 가능! [warn] -> 해당 행 열에 여러 나무가 있어야 하므로 삼중 리스트

봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1증가
    - 나이가 어린 나무부터
    - 내 나이만큼 못 먹는 나무는 죽음 [(나이)]
    
    각 칸마다...
        필요한 것: 죽는 나무들(나이), 나이가 5의 배수인 나무(위치)
        기존 꺼 복사, 바로 넣기
여름
    - 봄에 죽은 나무가 양분으로 변한다. 
    - 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가. 소수점 버림
가을
    그 복사한 그래프에 이어서 진행...
    - 나이가 5의 배수인 나무 -> 번식
        - 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
겨울
    - 땅에 양분 추가 A[r][c] 만큼. 
'''
# trees = [[] * N for _ in range(N)]  # 빈 리스트는 * 으로 복사하면 얕은 복사돼서 주의

from collections import deque

N, M, K = map(int, input().split())

A = []
seed = [[5] * N for _ in range(N)]  # 양분
trees = [[[] for _ in range(N)] for _ in range(N)]
pos = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for _ in range(N):
    line = list(map(int, input().split()))
    A.append(line)


for _ in range(M):
    x, y, z = map(int, input().split())  # 나무의 x, y, 나이
    x -= 1
    y -= 1
    trees[x][y].append(z)  # 나이
    
for r in range(N):
    for c in range(N):
        trees[r][c].sort()
        trees[r][c] = deque(trees[r][c])

def print_trees():
    global trees
    for i in range(len(trees)):
        print(trees[i])

answer = 0


for tc in range(K):
    # 봄
    died = deque([])
    growing = deque([])
    new_trees = [[deque([]) for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            while trees[r][c]:
                age = trees[r][c].popleft()
                if seed[r][c] < age:  # 만약 나이만큼 못 먹으면 "양분을 먹지 못하고" 죽는다
                    died.append((r, c, age // 2))
                    continue
                seed[r][c] -= age
                new_trees[r][c].append(age + 1)
                if (age + 1) % 5 == 0:  # 가을에 번식할 나무
                    growing.append((r, c))
    
    # 여름
    while died:
        row, col, value = died.popleft()
        seed[row][col] += value
    
    # 가을
    while growing:
        row, col = growing.popleft()
        for i in range(8):
            nr, nc = row + pos[i][0], col + pos[i][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            
            new_trees[nr][nc].appendleft(1)  # 나이가 1인 나무가 생기는 것임
    
    # 겨울
    for rr in range(N):
        for cc in range(N):
            seed[rr][cc] += A[rr][cc]

    trees = new_trees


for r in range(N):
    for c in range(N):
        answer += len(trees[r][c])


print(answer)