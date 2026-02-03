'''
BOJ 17779 게리맨더링 2

입력:
N
A

구조:
- x, y, d1, d2 전부 돌면서 한 번씩 구역을 만들기
- 5번 구역은 경계선을 먼저 찍고 그 경계선 안쪽을 채우기
- 1~4번 구역은 5번 아닌 칸을 조건 나눠 인구 합을 더하기
- 가장 큰 구역 합 - 가장 작은 구역 합 최소
'''
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

total_sum = 0
for row in A:
    total_sum += sum(row)

ans = 10 ** 18

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 >= N: continue
                if y - d1 < 0: continue
                if y + d2 >= N: continue

                is_five = [[False] * N for _ in range(N)]

                for i in range(d1 + 1):
                    is_five[x + i][y - i] = True  # 1
                    is_five[x + d2 + i][y + d2 - i] = True  # 4
                for i in range(d2 + 1):
                    is_five[x + i][y + i] = True  # 2
                    is_five[x + d1 + i][y - d1 + i] = True  # 3

                s = [0] * 5

                for r in range(x + d1):
                    for c in range(y + 1):
                        if is_five[r][c]: break
                        s[0] += A[r][c]

                for r in range(x + d2 + 1):
                    for c in range(N - 1, y, -1):
                        if is_five[r][c]: break
                        s[1] += A[r][c]

                for r in range(x + d1, N):
                    for c in range(y - d1 + d2):
                        if is_five[r][c]: break
                        s[2] += A[r][c]

                for r in range(x + d2 + 1, N):
                    for c in range(N - 1, y - d1 + d2 - 1, -1):
                        if is_five[r][c]: break
                        s[3] += A[r][c]

                s[4] = total_sum - sum(s[:4])

                res = max(s) - min(s)
                if res < ans:
                    ans = res

print(ans)