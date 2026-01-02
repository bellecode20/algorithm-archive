# 입력 텍스트 파일 실행 코드
import sys
from pathlib import Path
BASE_DIR = Path(__file__).parent
sys.stdin = open(BASE_DIR / "input.txt", "r")
input = sys.stdin.readline

'''
보드판을 회전시켜서 구슬을 아래로 내려야 한다고 생각했는데 보드판을 회전시킬 필요는 없음
구슬이 움직이는 방향만 정해서 이동하면 된다.

빨간 구슬과 파란 구슬의 좌표를 visited 키로 사용한다.
이전에 어떤 순서로 기울였던 간에 두 좌표가 동일한 경우 다시 방문할 필요 없음
'''

from collections import deque
from copy import deepcopy


N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
answer = -1

visited = set()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_pos(target, grp):
    for r in range(len(grp)):
        for c in range(len(grp[0])):
            if grp[r][c] == target:
                return (r, c)

    return (int(1e9), int(1e9))


queue = deque()
queue.append((1, graph, []))  # 기울이기

is_success = False
while queue:

    depth, cur_graph, history = queue.popleft()

    if depth > 10:
        break
    
    cur_blue = get_pos("B", cur_graph)  # 기울이기 전 구슬 위치
    cur_red = get_pos("R", cur_graph)  # 기울이기 전 구슬 위치

    for turn in range(4):  # 기울이기
        copied_graph = deepcopy(cur_graph)

        # <이동하기>
        blue_r, blue_c = cur_blue
        red_r, red_c = cur_red
        blue_end, red_end = False, False
        while True:
            # 파란 공 이동
            next_br, next_bc = blue_r + dr[turn], blue_c + dc[turn]
            if copied_graph[next_br][next_bc] == "#":
                break
            if copied_graph[next_br][next_bc] == "O":
                blue_end = True
                blue_r, blue_c = next_br, next_bc
                break

            blue_r, blue_c = next_br, next_bc

        while True:
            # 빨간 공 이동
            next_rr, next_rc = red_r + dr[turn], red_c + dc[turn]
            if copied_graph[next_rr][next_rc] == "#":
                break
            if copied_graph[next_rr][next_rc] == "O":
                red_end = True
                red_r, red_c = next_rr, next_rc
                break

            red_r, red_c = next_rr, next_rc

        if blue_end:  # 파란 구슬이 구멍에 들어간 경우 실패
            continue

        # 겹쳐있는 경우 위치 조정하기. 원래 위치를 비교해서 더 멀리 있었던 구슬을 뒤로 한 칸 더 멀리 보낸다.
        if (blue_r, blue_c) == (red_r, red_c):
            if turn == 0:  # 위로 기울였던 경우
                if cur_blue[0] > cur_red[0]:  
                    blue_r += 1  # 빨간 구슬이 더 위에있었으므로 파란 구슬이 아래 행으로 간다.
                elif cur_blue[0] < cur_red[0]:
                    red_r += 1
            elif turn == 1:  # 오른쪽
                if cur_blue[1] < cur_red[1]:  
                    blue_c -= 1
                elif cur_blue[1] > cur_red[1]:
                    red_c -= 1
            elif turn == 2:  # 아래
                if cur_blue[0] > cur_red[0]:
                    red_r -= 1
                elif cur_blue[0] < cur_red[0]:
                    blue_r -= 1
            else:  # 왼쪽
                if cur_blue[1] < cur_red[1]:  
                    red_c += 1
                elif cur_blue[1] > cur_red[1]:
                    blue_c += 1
        
        if (blue_r, blue_c, red_r, red_c) in visited:  # 방문 처리
            continue

        # 방문처리
        visited.add((blue_r, blue_c, red_r, red_c))

        # 기존 위치는 빈 칸으로 수정
        copied_graph[cur_blue[0]][cur_blue[1]] = "."
        copied_graph[cur_red[0]][cur_red[1]] = "."

        # 기울인 후 위치한 곳으로 구슬 넣기
        copied_graph[blue_r][blue_c] = "B"
        copied_graph[red_r][red_c] = "R"
        
        if red_end:  # 빨간 구슬만 들어간 경우 성공
            answer = depth
            is_success = True
            break  
        
        queue.append((depth + 1, copied_graph, history + [turn]))
    
    if is_success:
        break

print(answer)