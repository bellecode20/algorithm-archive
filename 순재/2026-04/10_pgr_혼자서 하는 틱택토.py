def solution(data):
    o_cnt = sum(row.count('O') for row in data)
    x_cnt = sum(row.count('X') for row in data)

    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1):
        return 0

    def win(c):
        for i in range(3):
            if all(data[i][j] == c for j in range(3)):
                return True
            
        for j in range(3):
            if all(data[i][j] == c for i in range(3)):
                return True

        if all(data[i][i] == c for i in range(3)):
            return True
        
        if all(data[i][2 - i] == c for i in range(3)):
            return True

        return False

    o_win = win('O')
    x_win = win('X')

    if o_win and x_win:
        return 0
    if o_win and o_cnt != x_cnt + 1:
        return 0
    if x_win and o_cnt != x_cnt:
        return 0

    return 1