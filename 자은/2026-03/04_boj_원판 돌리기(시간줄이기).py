from collections import deque

def is_same(x,y):
    num=arr[x][y]
    if num==0:return
    if num==arr[x][(y+1)%M]:
        same.add((x,y))
        same.add((x,(y+1)%M))

    if x<N and arr[x+1][y]==num:
        same.add((x,y))
        same.add((x+1,y))


N,M,T=map(int,input().split())
arr=[[0]*M]+[deque(map(int,input().split())) for _ in range(N)]
result=0
for _ in range(T):
    x,d,k=map(int,input().split())

    for i in range(x,N+1,x):
        if d==0:
            arr[i].rotate(k)
        elif d==1:
            arr[i].rotate(-k)

    same=set()
    sm=0
    cnt=0
    for i in range(1,N+1):
        for j in range(M):
            if arr[i][j]:
                is_same(i,j)
                cnt+=1
                sm+=arr[i][j]
    if same:
        for r,c in same:
            arr[r][c]=False
    elif cnt>0:
        av=sm/cnt
        for i in range(1,N+1):
            for j in range(M):
                if arr[i][j]:
                    if arr[i][j]<av:
                        arr[i][j]+=1
                    elif arr[i][j]>av:
                        arr[i][j]-=1
    elif cnt==0:break

for i in range(1,N+1):
    for j in range(M):
        if arr[i][j]:
            result+=arr[i][j]

print(result)