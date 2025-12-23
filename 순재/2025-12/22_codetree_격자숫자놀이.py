def play(lst):
    global time
    new_data = []
    mx_len = 0

    for lst_r in lst:
        cnt = {}
        for num in lst_r:
            if num == 0:
                continue
            cnt[num] = cnt.get(num, 0) + 1

        pair = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        row_count = 0

        for num, count in pair:
            if row_count + 2 > 100:
                break
            
            new_row.extend([num, count])
            row_count += 2

        mx_len = max(mx_len, len(new_row))
        new_data.append(new_row)

    for new_data_row in new_data:
        new_data_row.extend([0] * (mx_len - len(new_data_row)))

    lst[:] = new_data
    time += 1

r, c, k = map(int, input().split())
r -= 1
c -= 1
data = [list(map(int, input().split())) for _ in range(3)]
time = 0

while True:
    r_len = len(data)
    c_len = len(data[0])
    
    if r < r_len and c < c_len and data[r][c] == k:
        break

    if time > 100:
        break

    if r_len >= c_len:
        play(data)
    else:
        data = list(map(list, zip(*data)))
        play(data)
        data = list(map(list, zip(*data)))

if time <= 100:
    print(time)
else:
    print(-1)