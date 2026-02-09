N = int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())
cnt=0
for i in range(N):
    if A[i]>0:
        A[i]-=B
        cnt+=1
for a in A:
    if a<=0:continue
    if a>C:
        if a%C==0:cnt+=a//C
        else: cnt+=a//C+1
    else: cnt+=1
    
print(cnt)
