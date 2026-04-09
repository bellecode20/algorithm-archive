'''
BOJ 17779 게리맨더링 2

입력:
N
graph

구조:

일단 다 돌기
5번 처리 우선?
하면 틀림

경계 만나면 중단?
비교하면서 계속 진행
'''


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

total = 0
for r in range(N):
    for c in range(N):
        total += graph[r][c]

ans = float('inf')

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 >= N:
                    continue
                if y - d1 < 0:
                    continue
                if y + d2 >= N:
                    continue

                border = [[0] * N for _ in range(N)]

                for i in range(d1 + 1):
                    border[x + i][y - i] = 1
                    border[x + d2 + i][y + d2 - i] = 1

                for i in range(d2 + 1):
                    border[x + i][y + i] = 1
                    border[x + d1 + i][y - d1 + i] = 1

                people = [0] * 5


                for r in range(x + d1):
                    for c in range(y + 1):
                        if border[r][c] == 1:
                            break
                        people[0] += graph[r][c]


                for r in range(x + d2 + 1):
                    for c in range(N - 1, y, -1):
                        if border[r][c] == 1:
                            break
                        people[1] += graph[r][c]


                for r in range(x + d1, N):
                    for c in range(y - d1 + d2):
                        if border[r][c] == 1:
                            break
                        people[2] += graph[r][c]

                for r in range(x + d2 + 1, N):
                    for c in range(N - 1, y - d1 + d2 - 1, -1):
                        if border[r][c] == 1:
                            break
                        people[3] += graph[r][c]

                people[4] = total
                for i in range(4):
                    people[4] -= people[i]

                diff = max(people) - min(people)
                if diff < ans:
                    ans = diff

print(ans)