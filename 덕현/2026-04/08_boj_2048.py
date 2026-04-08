'''
BOJ 12100 2048 (Easy)

입력:
N
graph

구조:
5번 이동하고 한 줄 보고 0 없애기
같은 수 == 합치기
남는 칸 == 0
다하면 최대값
'''

def get_biggest(arr):
    mx = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > mx:
                mx = arr[r][c]
    return mx

def make_line(line):
    nums = []

    for x in line:
        if x != 0:
            nums.append(x)

    res = []
    idx = 0

    while idx < len(nums):
        if idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
            res.append(nums[idx] * 2)
            idx += 2
        else:
            res.append(nums[idx])
            idx += 1

    while len(res) < N:
        res.append(0)

    return res

def move(arr, d):
    new = []
    for i in range(N):
        new.append([0] * N)

    if d == 0:   # 상
        for c in range(N):
            line = []
            for r in range(N):
                line.append(arr[r][c])

            line = make_line(line)

            for r in range(N):
                new[r][c] = line[r]

    elif d == 1: # 하
        for c in range(N):
            line = []
            for r in range(N - 1, -1, -1):
                line.append(arr[r][c])

            line = make_line(line)

            idx = 0
            for r in range(N - 1, -1, -1):
                new[r][c] = line[idx]
                idx += 1

    elif d == 2: # 좌
        for r in range(N):
            line = []
            for c in range(N):
                line.append(arr[r][c])

            line = make_line(line)

            for c in range(N):
                new[r][c] = line[c]

    else:        # 우
        for r in range(N):
            line = []
            for c in range(N - 1, -1, -1):
                line.append(arr[r][c])

            line = make_line(line)

            idx = 0
            for c in range(N - 1, -1, -1):
                new[r][c] = line[idx]
                idx += 1

    return new

def dfs(cnt, arr):
    global ans

    if cnt == 5:
        big = get_biggest(arr)
        if big > ans:
            ans = big
        return

    for d in range(4):
        next_arr = move(arr, d)
        dfs(cnt + 1, next_arr)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = get_biggest(graph)
dfs(0, graph)

print(ans)