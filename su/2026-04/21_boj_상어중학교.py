from collections import defaultdict, deque
# -2: 빈칸, -1: 검, 0: 무지개, 기타: 일반

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
 
def bfs(row, col):
    global visited

    group_list = [(row, col)]
    visited.add((row, col))
    cnt = 1
    color = board[row][col]
    queue = deque([(row, col)])
    rainbow = []


    while queue:
        cur_row, cur_col = queue.popleft()
        for i in range(4):
            nr = cur_row + dr[i]
            nc = cur_col + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if (nr , nc) in visited:
                continue
            if board[nr][nc] not in (0, color):
                continue
            
            # if board[nr][nc] == -1 or (board[nr][nc] > 0 and board[nr][nc] != color):  # 오류: -2 안걸러짐
            #     continue
            
            queue.append((nr, nc))
            visited.add((nr, nc))
            group_list.append((nr, nc))
            cnt += 1
            if board[nr][nc] == 0:
                rainbow.append((nr, nc))
    
    # 무지개 visited 해제
    for r, c in rainbow:
        visited.remove((r, c))

    return group_list, cnt, len(rainbow)

def get_ref(cells):
    cells.sort(key=lambda x: (x[0], x[1]))
    for i, j in cells:
        if board[i][j] == 0:
            continue
        return (i, j)

    return (int(1e9), int(1e9))

def delete_group():
    global candidates
    key_block = (candidates[0][2], candidates[0][3])
    for r, c in groups[key_block]:
        board[r][c] = -2

def pprint(brd):
    for i in range(len(brd)):
        print(brd[i])
    

def gravitate():
    global board
    
    for c in range(N):
        pointer = N - 1

        for r in range(N -1, -1, -1):
            if board[r][c] == -1:  # 검은 블록
                pointer = r - 1
            elif board[r][c] >= 0:  # 일반 블록, 무지개
                board[pointer][c] = board[r][c]
                if pointer != r:
                    board[r][c] = -2

                pointer -= 1


def rotate():
    # 반시계 회전
    global board
    new_board = [[-2] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_board[N - col - 1][row] = board[row][col]
    
    board = new_board  # 갱신 🔥

while True:
    visited = set()
    candidates = []
    groups = defaultdict(list)

    for r in range(N):
        for c in range(N):
            if board[r][c] > 0 and (r, c) not in visited:  # 일반 블록인 경우
                group_list, group_cnt, rainbow_cnt = bfs(r, c)  # 그룹 멤버 찾기
                if group_cnt < 2:  # 블록의 개수가 1인 경우 넘어가기
                    continue
                ref_pos = get_ref(group_list)  # 기준 블록 찾기
                groups[ref_pos] = group_list  # 기준 블록으로 그룹 리스트 저장
                candidates.append((group_cnt, rainbow_cnt, ref_pos[0], ref_pos[1]))  # 삭제할 리스트 후보 만들기
    
    # 만약에 그룹이 존재하지 않는 경우 멈추기
    if not groups:
        break

    candidates.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    answer += candidates[0][0] ** 2
    delete_group()
    gravitate()
    rotate()
    gravitate()


print(answer)


'''
다른 풀이

from collections import deque

# -2: 빈칸, -1: 검은 블록, 0: 무지개

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

answer = 0


def bfs(sr, sc, visited):
    q = deque([(sr,sc)])
    group = [(sr,sc)]
    visited[sr][sc] = True
    color = board[sr][sc]

    rainbow = []
    rainbow_cnt = 0

    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr<0 or nc<0 or nr>=N or nc>=N:
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == -1:
                continue
            if board[nr][nc] != 0 and board[nr][nc] != color:
                continue

            visited[nr][nc] = True
            q.append((nr,nc))
            group.append((nr,nc))

            if board[nr][nc] == 0:
                rainbow_cnt += 1
                rainbow.append((nr,nc))

    # 무지개 visited 해제
    for r,c in rainbow:
        visited[r][c] = False

    return group, rainbow_cnt


def gravity():
    for c in range(N):
        pointer = N-1

        for r in range(N-1,-1,-1):

            if board[r][c] == -1:
                pointer = r-1

            elif board[r][c] >= 0:

                block = board[r][c]
                board[r][c] = -2

                board[pointer][c] = block
                pointer -= 1


def rotate():
    new_board = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            new_board[N-1-c][r] = board[r][c]

    return new_board


while True:

    visited = [[False]*N for _ in range(N)]
    candidates = []

    for r in range(N):
        for c in range(N):

            if board[r][c] > 0 and not visited[r][c]:

                group, rainbow_cnt = bfs(r,c,visited)

                if len(group) < 2:
                    continue

                # 기준 블록 찾기
                normals = [p for p in group if board[p[0]][p[1]] > 0]
                normals.sort()
                ref_r, ref_c = normals[0]

                candidates.append((len(group), rainbow_cnt, ref_r, ref_c, group))

    if not candidates:
        break

    candidates.sort(key=lambda x:(-x[0],-x[1],-x[2],-x[3]))

    group = candidates[0][4]

    answer += len(group)**2

    # 그룹 삭제
    for r,c in group:
        board[r][c] = -2

    gravity()
    board = rotate()
    gravity()


print(answer)

'''