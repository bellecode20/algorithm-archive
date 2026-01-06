'''
BOJ 21608 상어 초등학교

규칙대로 자리 배치
1. 좋아하는 학생이 인접(상하좌우)한 칸 수가 최대
2. (1 동률) 인접한 빈 칸 수가 최대
3. (2 동률) 행 번호가 가장 작은 칸
4. (3 동률) 열 번호가 가장 작은 칸

배치가 끝난 후 만족도 점수:
인접 좋아하는 학생 수 = 0,1,2,3,4 -> 0,1,10,100,1000

입력:
N
N^2 줄: 학생번호 a, 좋아하는 학생 4명

구조:
- order 리스트로 학생 배치 순서 저장
- like[a] = set(좋아하는 학생들)
- seat[a] = (r,c)
- 매 학생마다 모든 빈 칸을 훑으며 (좋아 인접수, 빈칸 인접수, r, c) 중 최적 선택
- 마지막에 점수 계산
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def count_empty(r, c, a):
    like_cnt = 0
    empty_cnt = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] == 0:
                empty_cnt += 1
            elif grid[nr][nc] in like[a]:
                like_cnt += 1
    return like_cnt, empty_cnt


N = int(input())
like = dict()
order = []

for _ in range(N * N):
    arr = list(map(int, input().split()))
    a = arr[0]
    like[a] = set(arr[1:])
    order.append(a)

grid = [[0] * N for _ in range(N)]
pos = dict()


for a in order:
    best = (-1, -1, N, N)  # r,c는 작을수록 좋음
    br = bc = -1

    for r in range(N):
        for c in range(N):
            if grid[r][c] != 0:
                continue
            like_cnt, empty_cnt = count_empty(r, c, a)

            cand = (like_cnt, empty_cnt, -r, -c)
            cur = (best[0], best[1], -best[2], -best[3])

            if cand > cur:
                best = (like_cnt, empty_cnt, r, c)
                br, bc = r, c

    grid[br][bc] = a
    pos[a] = (br, bc)

score_table = [0, 1, 10, 100, 1000]
ans = 0

for a in order:
    r, c = pos[a]
    like_cnt = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] in like[a]:
                like_cnt += 1
    ans += score_table[like_cnt]

print(ans)