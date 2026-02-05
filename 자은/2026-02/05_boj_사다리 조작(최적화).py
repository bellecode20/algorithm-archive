'''
잼미니가 알려준 최적화 방법
'''

def go():
    for n in range(1, N + 1):
        curr_c = n
        for r in range(1, H + 1):
            if isConnected[r][curr_c]:curr_c += 1
            elif curr_c > 1 and isConnected[r][curr_c - 1]:curr_c -= 1
        if curr_c != n: return False
    return True

def dfs(cnt, r_idx, c_idx):
    global result

    if go():
        result = min(result, cnt)
        return

    if cnt == 3 or cnt >= result:return

    for r in range(r_idx, H + 1):
        start_c = c_idx if r == r_idx else 1
        for c in range(start_c, N):
            if not isConnected[r][c] and not isConnected[r][c-1] and not isConnected[r][c+1]:
                isConnected[r][c] = True
                dfs(cnt + 1, r, c + 2) 
                isConnected[r][c] = False

N, M, H = map(int, input().split())
isConnected = [[False] * (N + 2) for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    isConnected[a][b] = True
result = 4
dfs(0, 1, 1)
if result <= 3:
    print(result)
else:print(-1)