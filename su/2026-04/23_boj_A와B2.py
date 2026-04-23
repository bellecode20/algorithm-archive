S = input().strip()
T = input().strip()

# T에서 시작해서 S까지 도달하기 (역방향)

def dfs(txt):
    if len(txt) == len(S):
        return 1 if txt == S else 0

    if txt[-1] == 'A':
        if dfs(txt[:-1]):
            return 1

    if txt[0] == 'B':
        if dfs(txt[1:][::-1]):
            return 1

    return 0

print(dfs(T))