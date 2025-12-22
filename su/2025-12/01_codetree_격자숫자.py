import sys
from collections import Counter

# input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1

A = [list(map(int, input().split())) for _ in range(3)]
max_r, max_c = 3, 3  # 현재 유효 행/열 크기

def operate_R(arr, max_r, max_c):
    new_rows = []
    new_max_c = 0

    for i in range(max_r):
        row = arr[i][:max_c]
        # 0 제거
        row = [x for x in row if x != 0]

        cnt = Counter(row)
        pairs = list(cnt.items())  # (num, freq)
        pairs.sort(key=lambda x: (x[1], x[0]))

        new_row = []
        for num, freq in pairs:
            new_row.extend([num, freq])
            if len(new_row) >= 100:
                new_row = new_row[:100]
                break

        new_max_c = max(new_max_c, len(new_row))
        new_rows.append(new_row)

    # 패딩(0 채우기) + 100 제한
    for i in range(len(new_rows)):
        if len(new_rows[i]) < new_max_c:
            new_rows[i].extend([0] * (new_max_c - len(new_rows[i])))

    # new_max_c도 최대 100
    new_max_c = min(new_max_c, 100)

    # 100*100 저장소로 복사
    new_arr = [[0] * 100 for _ in range(100)]
    for i in range(max_r):
        row = new_rows[i]
        for j in range(new_max_c):
            new_arr[i][j] = row[j]

    return new_arr, max_r, new_max_c

def operate_C(arr, max_r, max_c):
    # 열 단위로 같은 작업
    new_cols = []
    new_max_r = 0

    for j in range(max_c):
        col = [arr[i][j] for i in range(max_r)]
        col = [x for x in col if x != 0]

        cnt = Counter(col)
        pairs = list(cnt.items())
        pairs.sort(key=lambda x: (x[1], x[0]))

        new_col = []
        for num, freq in pairs:
            new_col.extend([num, freq])
            if len(new_col) >= 100:
                new_col = new_col[:100]
                break

        new_max_r = max(new_max_r, len(new_col))
        new_cols.append(new_col)

    for j in range(len(new_cols)):
        if len(new_cols[j]) < new_max_r:
            new_cols[j].extend([0] * (new_max_r - len(new_cols[j])))

    new_max_r = min(new_max_r, 100)

    new_arr = [[0] * 100 for _ in range(100)]
    for j in range(max_c):
        col = new_cols[j]
        for i in range(new_max_r):
            new_arr[i][j] = col[i]

    return new_arr, new_max_r, max_c

# 초기 A를 100x100 저장소로 확장
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    for j in range(3):
        arr[i][j] = A[i][j]

ans = -1
for t in range(101):  # 0초부터 100초까지 확인
    if 0 <= r < max_r and 0 <= c < max_c and arr[r][c] == k:
        ans = t
        break
    if t == 100:
        break

    if max_r >= max_c:
        arr, max_r, max_c = operate_R(arr, max_r, max_c)
    else:
        arr, max_r, max_c = operate_C(arr, max_r, max_c)

print(ans)
