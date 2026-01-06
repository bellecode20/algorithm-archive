from collections import deque

def rotate(num, dir):
    if dir == 1:
        gears[num].rotate(1)
    else:
        gears[num].rotate(-1)

gears = [None]
for _ in range(4):
    gears.append(deque(map(int, input().strip())))

k = int(input())
orders = [tuple(map(int, input().split())) for _ in range(k)]


for num, dir in orders:
    rotate_dir = [0] * 5
    rotate_dir[num] = dir

    d = dir
    for i in range(num, 1, -1):
        if gears[i][6] != gears[i - 1][2]:
            d = -d
            rotate_dir[i - 1] = d
        else:
            break

    d = dir
    for i in range(num, 4):
        if gears[i][2] != gears[i + 1][6]:
            d = -d
            rotate_dir[i + 1] = d
        else:
            break

    for i in range(1, 5):
        if rotate_dir[i] != 0:
            rotate(i, rotate_dir[i])

ans = 0
for i in range(1, 5):
    if gears[i][0] == 1:
        ans += 2 ** (i - 1)

print(ans)