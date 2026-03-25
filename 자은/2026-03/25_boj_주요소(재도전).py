N=int(input())
distance=list(map(int,input().split()))
costs=list(map(int,input().split()))
result=0
mn_cost=costs[0]

for i in range(N-1):
    if costs[i]<mn_cost:
        mn_cost=costs[i]
    result+=distance[i]*mn_cost
    
print(result)