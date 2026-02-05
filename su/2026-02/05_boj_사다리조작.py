# https://www.acmicpc.net/problem/15684


'''
시간초과 -> 가지치기 조건 추가해서 수정해야 하는 코드입니다.
'''

N, M, H = map(int, input().split())
ladder = [[False] * (N-1) for _ in range(H)]
answer = int(1e9)

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = True

def simulate():
    global ladder

    for start_col in range(N):
        col = start_col
        for row in range(H):
            # 오른쪽 
            if col < N - 1 and ladder[row][col]:
                col += 1
            elif col > 0 and ladder[row][col - 1]:
                col -= 1
        
        if col != start_col:
            return False
                
    return True

def dfs(depth):  # 가로선 위치, depth
    global answer

    if simulate():
        answer = min(depth, answer)
        return

    if depth == 3 or depth >= answer:
        return

    for row in range(H):
        for col in range(N-1):
            if not ladder[row][col] and (col == 0 or not ladder[row][col-1]) and (col == N-2 or not ladder[row][col+1]):
                ladder[row][col] = True
                dfs(depth + 1)
                ladder[row][col] = False

dfs(0)
print(answer if answer != int(1e9) else -1)