'''
BOJ 16987 계란으로 계란치기

입력:
N
s
w


구조:
idx번째 계란을 들고, 다른 계란 하나를 친다
서로 내구도 깎는다
깨졌으면 카운트
끝까지 돌려서 최대값
'''

N = int(input())
s = []
w = []
for _ in range(N):
    a, b = map(int, input().split())
    s.append(a)
    w.append(b)

ans = 0

def dfs(idx, broken):
    global ans

    if idx == N:
        if broken > ans:
            ans = broken
        return

    if s[idx] <= 0:
        dfs(idx + 1, broken)
        return

    hit = False
    for j in range(N):
        if j == idx:
            continue
        if s[j] <= 0:
            continue

        hit = True

        si = s[idx]
        sj = s[j]

        s[idx] -= w[j]
        s[j] -= w[idx]

        add = 0
        if si > 0 and s[idx] <= 0:
            add += 1
        if sj > 0 and s[j] <= 0:
            add += 1

        dfs(idx + 1, broken + add)

        s[idx] = si
        s[j] = sj

    if not hit:
        dfs(idx + 1, broken)

dfs(0, 0)
print(ans)
