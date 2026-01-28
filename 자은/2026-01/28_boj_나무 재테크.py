from collections import deque
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)
ground = [[5]*N for _ in range(N)]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:continue
            new_trees,dead=deque(),0
            for age in trees[i][j]:
                if ground[i][j]>= age:
                    ground[i][j]-=age
                    new_trees.append(age+1)
                else:dead+=age//2
            trees[i][j]=new_trees
            ground[i][j]+=dead

    for i in range(N):
        for j in range(N):
            cnt=0
            for age in trees[i][j]:
                if age%5==0:
                    cnt+=1
            if cnt:
                for d in range(8):
                    nx,ny=i+dx[d],j+dy[d]
                    if nx<0 or nx>=N or ny<0 or ny>=N:continue
                    for _ in range(cnt):
                        trees[nx][ny].appendleft(1)
            ground[i][j]+=A[i][j]
result=sum(len(trees[i][j]) for i in range(N) for j in range(N))
print(result)