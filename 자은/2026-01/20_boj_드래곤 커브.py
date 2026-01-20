dx = [0,-1,0,1]
dy = [1,0,-1,0]

N=int(input())
arr = [[0]*101 for _ in range(101)]
total=0

for _ in range(N):
    y,x,d,g = map(int,input().split())
    lst=[]
    lst.append((x,y))
    lst.append((x+dx[d],y+dy[d]))

    for _ in range(g):
        end_x,end_y=lst[-1]

        for i in range(len(lst)-2,-1,-1):
            cx, cy= lst[i]
            lst.append((end_x-(end_y-cy),end_y+(end_x-cx)))
    
    for i,j in lst:
        arr[i][j]=1

for i in range(100):
    for j in range(100):
        if arr[i][j]==arr[i][j+1]==arr[i+1][j]==arr[i+1][j+1]==1:
            total+=1

print(total)
