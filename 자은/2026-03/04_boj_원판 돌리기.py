def is_same(x,y):
    num=arr[x][y]
    if num==arr[x][(y-1)%M] or num==arr[x][(y+1)%M]:
        return True
    if x>1 and arr[x-1][y]==num:
        return True
    if x<N and arr[x+1][y]==num:
        return True
    return False

N,M,T=map(int,input().split())
arr=[[0]*M]+[list(map(int,input().split())) for _ in range(N)]
result=0
for _ in range(T):
    x,d,k=map(int,input().split())

    for i in range(x,N+1,x):
        if d==0:
            for _ in range(k):
                arr[i]=[arr[i][-1]]+arr[i][:-1]
        elif d==1:
            for _ in range(k):
                arr[i]=arr[i][1:]+[arr[i][0]]
    same=[]
    sm=0
    cnt=0
    for i in range(1,N+1):
        for j in range(M):
            if arr[i][j]:
                if is_same(i,j):
                    same.append((i,j))
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
    elif cnt==0:
        break
for i in range(1,N+1):
    for j in range(M):
        if arr[i][j]:
            result+=arr[i][j]

print(result)