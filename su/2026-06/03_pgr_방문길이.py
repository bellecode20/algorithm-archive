'''
이차원 배열을 직접 만드는 경우 좌표 설정 및 경계 처리가 복잡해서
좌표만 설정 후 값 갱신하는 방식으로 진행
'''

def solution(dirs):
    answer = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]  # U R D L
    n = len(dirs)
    SIZE = 5
    directions = {
        "U": 0,
        "R": 1,
        "D": 2,
        "L": 3
    }
    
    visited_cells = set()
    row = col = 0
    
    for i in range(n):
        d = directions[dirs[i]]
        nr, nc = row + dr[d], col + dc[d]
        if nr < -SIZE or nc < -SIZE or nr > SIZE or nc > SIZE:
            continue
        
        visited_cells.add((row, col, nr, nc))
        visited_cells.add((nr, nc, row, col))
        row, col = nr, nc
        
    answer = len(visited_cells) // 2
    return answer