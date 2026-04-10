'''
프로그래머스 혼자서 하는 틱택토

입력:
board ch

구조:
O X 개수 세고 빙고 확인
개수 조건 먼저 빙고 상태 확인 ㄱ
'''
def solution(board):
    o = 0
    x = 0

    for r in range(3):
        for c in range(3):
            if board[r][c] == 'O':
                o += 1
            elif board[r][c] == 'X':
                x += 1

    if not (o == x or o == x + 1):
        return 0

    ow = 0
    xw = 0

    for r in range(3):
        ok_o = 1
        ok_x = 1
        for c in range(3):
            if board[r][c] != 'O':
                ok_o = 0
            if board[r][c] != 'X':
                ok_x = 0
        if ok_o:
            ow = 1
        if ok_x:
            xw = 1

    for c in range(3):
        ok_o = 1
        ok_x = 1
        for r in range(3):
            if board[r][c] != 'O':
                ok_o = 0
            if board[r][c] != 'X':
                ok_x = 0
        if ok_o:
            ow = 1
        if ok_x:
            xw = 1

    ok_o = 1
    ok_x = 1
    for i in range(3):
        if board[i][i] != 'O':
            ok_o = 0
        if board[i][i] != 'X':
            ok_x = 0
    if ok_o:
        ow = 1
    if ok_x:
        xw = 1

    ok_o = 1
    ok_x = 1
    for i in range(3):
        if board[i][2 - i] != 'O':
            ok_o = 0
        if board[i][2 - i] != 'X':
            ok_x = 0
    if ok_o:
        ow = 1
    if ok_x:
        xw = 1

    if ow and xw:
        return 0

    if ow and o != x + 1:
        return 0

    if xw and o != x:
        return 0

    return 1