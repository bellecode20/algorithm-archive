from collections import deque

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def Union(x,y):
    global finish
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    group=set()
    group.add((x,y))
    person_sum=people[x][y]

    while q:
        cx, cy = q.popleft()
        
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if visited[nx][ny]:
                continue
            if L<=abs(people[cx][cy]-people[nx][ny])<=R:
                finish = False
                group.add((nx,ny))
                visited[nx][ny]=1
                person_sum+=people[nx][ny]
                q.append((nx,ny))

    if len(group)==1:
        return
    
    population=person_sum//len(group)
    for r,c in group:
        people[r][c]=population

def is_possible(x,y):

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N:
            continue
        if visited[nx][ny]:
            continue
        if L <= abs(people[x][y]-people[nx][ny]) <= R:
            return True
    return False


N, L, R = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(N)]
result = -1


while True:
    finish = True
    visited=[[0]*N for _ in range(N)]
    result+=1

    for i in range(N):
        for j in range(N):
            possible=is_possible(i,j)
            if not visited[i][j] and possible:
                Union(i,j)
    
    if finish:
        break

print(result)

