import sys
input = sys.stdin.readline

def get_max(board):
    return max(map(max, board))

def move(board, n):
    new_board = []
    for row in board:
        # 1. 0 제외 숫자 추출
        temp = [v for v in row if v != 0]
        # 2. 합치기
        new_row = []
        skip = False
        for i in range(len(temp)):
            if skip:
                skip = False
                continue
            if i + 1 < len(temp) and temp[i] == temp[i+1]:
                new_row.append(temp[i] * 2)
                skip = True
            else:
                new_row.append(temp[i])
        # 3. 나머지 0 채우기 (리스트 컴프리헨션으로 속도 향상)
        new_board.append(new_row + [0] * (n - len(new_row)))
    return new_board

def rotate_90(board, n):
    """보드 시계방향 90도 회전"""
    return [list(row) for row in zip(*board[::-1])]

def solve(board, count):
    global max_val
    
    # 현재 단계에서 가질 수 있는 최대값 확인
    current_max = get_max(board)
    if count == 5:
        max_val = max(max_val, current_max)
        return

    # 가지치기: 현재 보드 최대값에서 남은 횟수만큼 모두 합쳐져도 max_val보다 작으면 리턴
    if current_max * (2 ** (5 - count)) <= max_val:
        return

    for _ in range(4):
        moved_board = move(board, N)
        # 보드가 변하지 않았다면 다음 방향으로 (불필요한 재귀 방지)
        if moved_board != board:
            solve(moved_board, count + 1)
        else:
            # 변하지 않았어도 끝까지는 확인해야 하므로 max_val만 갱신
            max_val = max(max_val, current_max)
            
        board = rotate_90(board, N)

N = int(input())
initial_board = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
solve(initial_board, 0)
print(max_val)