# https://www.acmicpc.net/problem/17779


'''
테케 실패.. 수정 중인 코드입니다
'''
from collections import deque

N = int(input())
board = [[-1] * (N + 2) for _ in range(N+2)]

for i in range(1, N+1):
    board[i][1:N+1] = list(map(int, input().split()))

# board = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)

def pprint(brd):
    for i in range(len(brd)):
        print(brd[i])

pprint(board)

def fill_inside(district, num, sr, sc):
    for row in range(1, N+1):
        s = N+1
        e = 0
        for col in range(1, N+1):
            if district[row][col] == 5:
                s = min(col, s)
                e = max(col, e)
        
        if s == N+1 or e == 0:  # 한 개인 경우
            continue
        print(row, col, s+1, e)
        district[row][s+1:e] = [5] * (e - s - 1)

    return district

def fill_line(district, x, y):
    global d1, d2

    pos = [(1, -1), (1, 1), (-1, 1), (-1, -1)]  # 왼쪽아래 오른쪽아래 오른쪽위 왼쪽위 (1번, 3번, 2번, 4번)
    district[x][y] = 5  # 시작점
    r, c = x, y

    for i in range(4):
        while True:
            nr, nc = pos[i][0] + r, pos[i][1] + c
            if district[nr][nc] == -1:  # 보드판 밖
                break
            district[nr][nc] = 5
            r, c = nr, nc
            if (nr, nc) in [(x + d1, y - d1), (x+d2, y+d2), (x+d1+d2, y-d1+d2), (x, y)]:
                break
        

    if (d1, d2) == (2, 2):
        print("----------전")
        pprint(district)

    district = fill_inside(district, 5, x+1, y)  # 아래 행 부터 시작

    if (d1, d2) == (2, 2):
        print("----------후")
        pprint(district)
    return district

def fill_all(district):
    global x, y, d1, d2
    people = [0, 0, 0, 0]
    for num in range(1, 5):

        for row in range(1, N + 1):
            for col in range(1, N+1):
                print(row, col)
                if district[row][col] != 0 and district[row][col] != num:
                    continue
                if num == 1:
                    if 1 <= row < x+d1 and 1 <= col <= y:
                        district[row][col] = num
                    else:
                        continue
                elif num == 2:
                    if 1 <= row <= x+d2 and y < col <= N:
                        district[row][col] = num
                    else:
                        continue
                elif num == 3:
                    if x+d1 <= row <= N and 1 <= col < y-d1+d2:
                        district[row][col] = num
                    else:
                        continue
                else:
                    if x+d2 < row <= N and y-d1+d2 <= col <= N:
                        district[row][col] = num
                    else:
                        continue
    
    for row in range(1, N+1):
        for col in range(1, N+1):
            num = district[row][col]
            people[num-1] += board[row][col]

    gap = max(people) - min(people)
    return gap

def divide(x, y, d1, d2):
    district = [[-1] * (N + 2) for _ in range(N + 2)]  # 선거구
    for i in range(1, N+1):
        district[i][1:N+1] = [0] * N

    district = fill_line(district, x, y)
    
    gap = fill_all(district)

    return gap


for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    answer = min(divide(x, y, d1, d2), answer)

print(answer)