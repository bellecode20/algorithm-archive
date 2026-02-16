'''
토마토 3차원
익은 토마토 1 안 익은 토마토 0 빈 칸 -1
델타 설정
dy = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
# 입력 데이터
M, N, H : 가로, 세로, 높이

# 구조
토마토 리스트 입력 (z,y,x)
1인 곳을 찾기
복사 필요 X
1인 곳의 좌표를 q에 넣어주고 시작.
bfs
for > 6 델타 탐색
끝나면 step 출력
'''
from collections import deque
dy = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs(graph):
    global step
    q = deque()
    for p,w,e in graph:
        q.append((p,w,e))
    step = -1
    while q:
        len_q = len(q)
        for _ in range(len_q):
            z,y,x = q.popleft()
            for k in range(6):
                nz = z + dz[k]
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = 1
                    q.append((nz,ny,nx))

        step += 1

    for h in range(H):
        for n in range(N):
            if tomato[h][n].count(0):
                step = -1
                return step

    return step

M, N, H = map(int,input().split())
tomato = []
ripe = []

for _ in range(H):
    tomato_lst = [list(map(int,input().split())) for _ in range(N)]
    tomato.append(tomato_lst)
 # z축, y축, x축
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                ripe.append((h,n,m))

print(bfs(ripe))