'''
BOJ 16235 나무 재테크

입력:
N, M, K
A
M

구조:
- 칸마다 나무 나이 리스트 오름차순
- 봄: 어린 나무부터 양분 먹고 +1, 못 먹으면 죽음
- 여름: 죽은 나무 나이//2 만큼 양분 추가
- 가을: 나이 % 5 == 0 이면 8방향에 나이 1 하고 나무 번식
- 겨울: A 양분 추가
'''

from collections import deque

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

nut = [[5] * N for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]

temp = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    temp[x - 1][y - 1].append(z)

for r in range(N):
    for c in range(N):
        if temp[r][c]:
            temp[r][c].sort()
            trees[r][c] = deque(temp[r][c])

for _ in range(K):
    for r in range(N):
        for c in range(N):
            if not trees[r][c]:
                continue

            cur = nut[r][c]
            alive = deque()
            dead_nutr = 0

            while trees[r][c]:
                age = trees[r][c].popleft()
                if cur >= age:
                    cur -= age
                    alive.append(age + 1)
                else:
                    dead_nutr += age // 2
                    while trees[r][c]:
                        dead_nutr += trees[r][c].popleft() // 2
                    break

            nut[r][c] = cur + dead_nutr
            trees[r][c] = alive

    breed = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not trees[r][c]:
                continue
            for age in trees[r][c]:
                if age % 5 == 0:
                    for k in range(8):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < N and 0 <= nc < N:
                            breed[nr][nc] += 1

    for r in range(N):
        for c in range(N):
            b = breed[r][c]
            if b:
                for _ in range(b):
                    trees[r][c].appendleft(1)

    for r in range(N):
        for c in range(N):
            nut[r][c] += A[r][c]


for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])

print(ans)
