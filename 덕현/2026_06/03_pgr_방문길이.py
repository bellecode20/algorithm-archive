'''
프로그래머스 49994 방문 길이

입력:
dirs

구조:
(0,0)부터 범위 해가지고 set에 저장
'''

def solution(dirs):
    visited = set()
    r = 0
    c = 0
    for op in dirs:
        nr = r
        nc = c
        if op == 'U':
            nr -= 1
        elif op == 'D':
            nr += 1
        elif op == 'L':
            nc -= 1
        else:
            nc += 1
        if nr < -5 or nr > 5 or nc < -5 or nc > 5:
            continue

        if (r, c) < (nr, nc):
            visited.add((r, c, nr, nc))
        else:
            visited.add((nr, nc, r, c))

        r = nr
        c = nc

    return len(visited)