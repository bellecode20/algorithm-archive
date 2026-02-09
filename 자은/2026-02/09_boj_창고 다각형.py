N=int(input())
sticks=[list(map(int,input().split())) for _ in range(N)]
sticks.sort()

mx_h=mx_idx=total=0
for i in range(N):
    if sticks[i][1]>mx_h:
        mx_h=sticks[i][1]
        mx_idx=i
#왼쪽
b_posit=sticks[0][0]
b_h=sticks[0][1]
for i in range(1,mx_idx+1):
    if sticks[i][1]>= b_h:
        total+=(sticks[i][0]-b_posit)*b_h
        b_posit=sticks[i][0]
        b_h=sticks[i][1]

#오른쪽
if mx_idx!=N-1:
    b_posit=sticks[N-1][0]
    b_h=sticks[N-1][1]
    for i in range(N-2,mx_idx-1,-1):
        if sticks[i][1]>= b_h:
            total+=(b_posit-sticks[i][0])*b_h
            b_posit=sticks[i][0]
            b_h=sticks[i][1]
total+=mx_h
print(total)