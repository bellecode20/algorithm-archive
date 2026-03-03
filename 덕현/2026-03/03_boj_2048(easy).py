'''
BOJ 12100 2048(easy)
입력:
N
graph

구조:
5번 이동까지 모든 방향을 다 해본다
한 번 움직일 때는
  - 0 빼고 모으기
  - 같은 수 붙어있으면 한 번만 합치기
  - 다시 빈칸 0 채우기
5번 끝났을 때 가장 큰 값
'''

def copy_board(board, n):
    temp = []
    for i in range(n):
        temp.append(board[i][:])
    return temp

def get_max(board, n):
    mx = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] > mx:
                mx = board[r][c]
    return mx

def merge_line(line, n):
    temp = []
    for x in line:
        if x != 0:
            temp.append(x)

    merged = []
    i = 0
    while i < len(temp):
        if i + 1 < len(temp) and temp[i] == temp[i + 1]:
            merged.append(temp[i] * 2)
            i += 2
        else:
            merged.append(temp[i])
            i += 1

    while len(merged) < n:
        merged.append(0)

    return merged

def move(board, n, d):
    res = [[0] * n for _ in range(n)]

    if d == 2:  # 왼
        for r in range(n):
            res[r] = merge_line(board[r], n)

    elif d == 3:  # 우
        for r in range(n):
            line = board[r][:]
            line.reverse()
            line = merge_line(line, n)
            line.reverse()
            res[r] = line

    elif d == 0:  # 상
        for c in range(n):
            line = []
            for r in range(n):
                line.append(board[r][c])
            line = merge_line(line, n)
            for r in range(n):
                res[r][c] = line[r]

    else:  #하
        for c in range(n):
            line = []
            for r in range(n - 1, -1, -1):
                line.append(board[r][c])
            line = merge_line(line, n)
            for r in range(n - 1, -1, -1):
                res[r][c] = line[n - 1 - r]

    return res

def dfs(depth, board):
    global ans, N
    if depth == 5:
        mx = get_max(board, N)
        if mx > ans:
            ans = mx
        return

    for d in range(4):
        nxt = move(board, N, d)
        dfs(depth + 1, nxt)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = get_max(graph, N)
dfs(0, graph)

print(ans)