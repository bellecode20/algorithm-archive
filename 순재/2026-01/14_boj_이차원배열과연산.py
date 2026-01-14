from collections import Counter

r, c, k = map(int, input().split())
r -= 1
c -= 1

data = [list(map(int, input().split())) for _ in range(3)]

time = 0

def r_operation(arr):
    new_arr = []
    max_len = 0
    for row in arr:
        cnt = Counter([x for x in row if x != 0])
        items = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, freq in items:
            new_row.append(num)
            new_row.append(freq)
        max_len = max(max_len, len(new_row))
        new_arr.append(new_row)
    for row in new_arr:
        while len(row) < max_len:
            row.append(0)
        if len(row) > 100:
            del row[100:]
    return new_arr

while time <= 100:
    if r < len(data) and c < len(data[0]) and data[r][c] == k:
        print(time)
        break

    time += 1

    if len(data) >= len(data[0]):
        data = r_operation(data)
    else:
        transposed = list(zip(*data))
        transposed = [list(row) for row in transposed]
        transposed = r_operation(transposed)
        data = list(map(list, zip(*transposed)))

    if time > 100:
        print(-1)
        break