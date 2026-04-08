from copy import deepcopy

def move_left(arr):
    new_data = []
    for row in arr:
        nums = []
        for x in row:
            if x != 0:
                nums.append(x)

        merged = []
        i = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                merged.append(nums[i] * 2)
                i += 2
            else:
                merged.append(nums[i])
                i += 1

        merged += [0] * (n - len(merged))
        new_data.append(merged)
    return new_data

def rotate(arr):
    return [list(row) for row in zip(*arr[::-1])]

def move(arr, d):
    temp = deepcopy(arr)
    for _ in range(d):
        temp = rotate(temp)
    temp = move_left(temp)
    for _ in range((4 - d) % 4):
        temp = rotate(temp)
    return temp

def dfs(dep, arr):
    global ans
    for i in range(n):
        for j in range(n):
            ans = max(ans, arr[i][j])
    if dep == 5:
        return
    for d in range(4):
        dfs(dep + 1, move(arr, d))

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, data)

print(ans)