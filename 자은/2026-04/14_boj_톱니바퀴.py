def right(n,d):
    if n>=3:return
    if wheels[n][2] != wheels[n+1][6]:
        rotate[n+1]=d*-1
        right(n+1,d*-1)

def left(n,d):
    if n<=0:return
    if wheels[n][6] != wheels[n-1][2]:
        rotate[n-1]=d*-1
        left(n-1,d*-1)

wheels=[list(map(int,input())) for _ in range(4)]
K=int(input())

for _ in range(K):
    rotate=[0]*4
    num,direction=map(int,input().split())
    num-=1
    rotate[num]=direction
    if num<3:right(num,direction)
    if num>0:left(num,direction)
    
    for i in range(len(rotate)):
        if rotate[i]==0:continue
        elif rotate[i]==1:wheels[i]=wheels[i][-1:]+wheels[i][:-1]
        elif rotate[i]==-1:wheels[i]=wheels[i][1:]+wheels[i][0:1]
answer=0
for i in range(4):
    if wheels[i][0]:answer+=2**i
print(answer)