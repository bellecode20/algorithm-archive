N=int(input())
h=list(map(int,input().split()))
can_see=[0]*N

for i in range(N-1):
    mx_value=float("-inf")
    for j in range(i+1,N):
        value=(h[j]-h[i])/(j-i)
        if value>mx_value:
            can_see[i]+=1
            can_see[j]+=1
            mx_value=value

print(max(can_see))