N = int(input())
eggs = []
answer = 0

for _ in range(N):
    S, W = map(int, input().split())  # 내구도, 무게
    eggs.append([S, W])


def dfs(idx):
    global answer

    if idx == N:
        cnt = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                cnt += 1

        answer = max(answer, cnt)
        return

    # 현재 계란이 이미 깨졌으면 다음으로
    if eggs[idx][0] <= 0:
        dfs(idx + 1)
        return

    is_hit_any = False

    for target in range(N):
        if target == idx:
            continue
        if eggs[target][0] <= 0:
            continue
        
        is_hit_any = True
        eggs[target][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[target][1]
        dfs(idx + 1)
        eggs[target][0] += eggs[idx][1]
        eggs[idx][0] += eggs[target][1]
    
    if not is_hit_any:
        dfs(idx + 1)

dfs(0)
print(answer)