import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# shark_pos[(r, c)] = 상어번호
shark_pos = {}

# shark_info[상어번호] = [속력, 방향, 크기]
shark_info = {}

for i in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1

    shark_pos[(r, c)] = i
    shark_info[i] = [s, d, z]

# 0: 위, 1: 아래, 2: 오른쪽, 3: 왼쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def catch_shark(fisher_col):
    """
    낚시왕이 현재 열에서 가장 가까운 상어를 잡는다.
    잡은 상어의 크기를 반환한다.
    """

    for row in range(R):
        if (row, fisher_col) in shark_pos:
            shark_idx = shark_pos[(row, fisher_col)]
            size = shark_info[shark_idx][2]

            del shark_pos[(row, fisher_col)]
            del shark_info[shark_idx]

            return size

    return 0


def move_sharks():
    global shark_pos, shark_info

    new_shark_pos = {}
    new_shark_info = {}

    for (row, col), shark_idx in shark_pos.items():
        s, d, z = shark_info[shark_idx]

        # 이동 횟수 줄이기
        if d == 0 or d == 1:
            cycle = 2 * (R - 1)
            move_count = s % cycle
        else:
            cycle = 2 * (C - 1)
            move_count = s % cycle

        # 상어 이동
        for _ in range(move_count):
            nr = row + dr[d]
            nc = col + dc[d]

            # 벽에 부딪히면 방향 반대
            if nr < 0 or nr >= R or nc < 0 or nc >= C:
                d ^= 1
                nr = row + dr[d]
                nc = col + dc[d]

            row, col = nr, nc

        # 이동 후 같은 칸에 상어가 있으면 큰 상어만 남김
        if (row, col) in new_shark_pos:
            prev_idx = new_shark_pos[(row, col)]
            prev_size = new_shark_info[prev_idx][2]

            if z > prev_size:
                del new_shark_info[prev_idx]
                new_shark_pos[(row, col)] = shark_idx
                new_shark_info[shark_idx] = [s, d, z]

        else:
            new_shark_pos[(row, col)] = shark_idx
            new_shark_info[shark_idx] = [s, d, z]

    shark_pos = new_shark_pos
    shark_info = new_shark_info


answer = 0

for fisher_col in range(C):
    # 1. 현재 열에서 가장 가까운 상어 잡기
    answer += catch_shark(fisher_col)

    # 2. 상어 이동
    move_sharks()

print(answer)

'''
예제 입력 1 
4 6 8
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4
3 3 1 2 7
1 5 8 4 3
3 6 2 1 2
2 2 2 3 5
예제 출력 1 
22


예제 입력 2 
100 100 0
예제 출력 2 
0

예제 입력 3 
4 5 4
4 1 3 3 8
1 3 5 2 9
2 4 8 4 1
4 5 0 1 4

예제 출력 3 
22

예제 입력 4 
2 2 4
1 1 1 1 1
2 2 2 2 2
1 2 1 2 3
2 1 2 1 4

예제 출력 4 
4

'''