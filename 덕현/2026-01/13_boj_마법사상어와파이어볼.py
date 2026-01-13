'''
BOJ 20056 마법사 상어와 파이어볼

입력:
N, M, K
fireballs: (r, c, m, s, d)

구조:
K번 반복
1) 이동해서 tmp에 모으기
2) tmp에서 같은 칸 처리(합치기/나누기)
3) graph 갱신
마지막 질량 합 출력
'''

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

N, M, K = map(int, input().split())
graph = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append((m, s, d))

for _ in range(K):
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for m, s, d in graph[r][c]:
                nr = (r + dr[d] * s) % N
                nc = (c + dc[d] * s) % N
                tmp[nr][nc].append((m, s, d))

    for r in range(N):
        for c in range(N):
            if len(tmp[r][c]) <= 1:
                continue

            cnt = len(tmp[r][c])
            msum = 0
            ssum = 0
            even = 0
            odd = 0

            for m, s, d in tmp[r][c]:
                msum += m
                ssum += s
                if d % 2 == 0:
                    even += 1
                else:
                    odd += 1

            nm = msum // 5
            if nm == 0:
                tmp[r][c] = []
                continue

            ns = ssum // cnt
            if even == cnt or odd == cnt:
                dirs = [0, 2, 4, 6]
            else:
                dirs = [1, 3, 5, 7]

            tmp[r][c] = [(nm, ns, nd) for nd in dirs]

    graph = tmp

ans = 0
for r in range(N):
    for c in range(N):
        for m, _, _ in graph[r][c]:
            ans += m

print(ans)
