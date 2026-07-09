new_board = []
dirc = [
    [(-1, -1), (-1, 0), (0, -1)],
    [(-1, 0), (-1, 1), (0, 1)],
    [(0, -1), (1, -1), (1, 0)],
    [(0, 1), (1, 0), (1, 1)]
]
deleted = set()
answer = 0

def visit(r, c, m, n):
    global deleted
    
    for pos in dirc:
        cnt = 0
        temp_del = set()
        temp_del.add((r, c))
        
        for dr, dc in pos:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= m or nc >= n:
                continue
            if new_board[nr][nc] != new_board[r][c]:
                continue

            cnt += 1
            temp_del.add((nr, nc))
            

        if cnt == 3:  # 4개 블록인 경우
            deleted = set(list(deleted) + list(temp_del))
            break


def delete_block():
    global deleted, new_board, answer
    for row, col in deleted:
        new_board[row][col] = ""

    answer += len(deleted)


def down_block(m, n):
    row = m - 1

    moved_board = []
    # print(n)
    mr = row
    mc = 0
    for i in range(m):
        moved_board.append([''] * n)
    
    # print(moved_board)

    while mc < n:
        if row == -1:  # row 초기화
            mc += 1
            row = m - 1
            mr = row
            continue

        if new_board[row][mc] != '':  # 블록인 경우 그대로 채워넣기
            moved_board[mr][mc] = new_board[row][mc]
            mr -= 1
            row -= 1
            continue
        
        # 빈공간인경우, new_board 인 애만 row 움직이기
        else:
            row -= 1

    return moved_board

def solution(m, n, board):
    global new_board, deleted, answer

    for i in range(m):
        new_board.append(list(board[i]))


    while True:
        deleted = set()

        for r in range(m):
            for c in range(n):
                if (r, c) in deleted or new_board[r][c] == "":  # 삭제되는 블록은 점검하지 않아도 됨
                    continue
                    
                visit(r, c, m, n)  # 삭제해야할 목록 체크
        
        if len(deleted) == 0:
            break

        delete_block()
        new_board = down_block(m, n)

    return answer